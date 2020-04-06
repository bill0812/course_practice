#!/usr/bin/env Rscript
install_packages <- function(){
    # check and install package
    if (!require("devtools")) {
        cat("Install package: devtools\n")
        install.packages("devtools",repos = "http://cran.us.r-project.org")
    } 
    if (!require("argparser")) {
        cat("Install package: argparser\n")
        install.packages("argparser",repos = "http://cran.us.r-project.org")
    } 
    if (!require("assertthat")) {
        cat("Install package: assertthat\n")
        install_github("hadley/assertthat")
    }
    if (!require("rpart")) {
        cat("Install package: rpart\n")
        install.packages("rpart",repos = "http://cran.us.r-project.org")
    } 
    suppressPackageStartupMessages(library("tools"))
    suppressPackageStartupMessages(library("devtools"))
    suppressPackageStartupMessages(library("argparser"))
    suppressPackageStartupMessages(library("assertthat"))
    suppressPackageStartupMessages(library("rpart"))
    cat("======================================\nAll package wad installed !\n")
}

get_args <- function(){
    # parser for each option
    args <- arg_parser("Calculate the mean and max value")
    args <- add_argument(args, "--fold", help="number of k which used in K-Fold cross validation")
    args <- add_argument(args, "--input", help="input csv files")
    args <- add_argument(args, "--output", help="output csv file")
    
    opt <- parse_args(args)
    return(opt)
}

check_args <- function(k_fold, output_file, input_file){
    
    if(k_fold<=2){
        stop("K should be more than two !")
    }
    
    # check output path
    if (!is.null(output_file)) {
        if (!dir.exists(dirname(output_file))) {
            output_dir = dirname(output_file)
            cat("Output Dir not exist ! Now Create one...\n")
            dir.create(output_dir, showWarnings = FALSE)
        }
        if (has_extension(output_file, 'csv') == FALSE) {
            stop("Output file is not csv !")
        }
    }
    # check input path and store data
    data = data.frame()
    if (!is.null(input_file)) {
        # check if the files exist
        if (!(file.exists(input_file) && !dir.exists(input_file))) {
            stop("Input file not exist !")
        }
        if (has_extension(input_file, 'csv') == FALSE) {
            stop("Input file is not csv !")
        }
        # read csv file's data
        # input_basename = file_path_sans_ext(basename(each_input_file))
        data <- read.csv(file=input_file, skip=1, header=F)
        
        # remove first column which is called id
        data$V1 = NULL
    }
    # success read files
    cat("Succeed loading all csv files !\n======================================\n")
    
    return(data)
}

print_status <- function(data, k_fold){
    # start cross validation and declare some variables
    total_sample <- nrow(data)
    train_sample <- floor((k_fold-2)/k_fold*nrow(data))
    valid_test_sample <- floor(0.5*(total_sample-train_sample))
    cat("Start Cross Validation...\n")
    cat("Fold ", k_fold, " \n")
    cat("Total Data: ", total_sample, "\n")
    cat("Total Training Data: ",train_sample, "\n")
    cat("Total Validation Data: ", valid_test_sample, "\n")
    cat("Total Testing Data: ", valid_test_sample, "\n")
}

sample_train_val_test <- function(data, k_fold){
    
    # use sample.int to sample training, validation, testing data
    train_sample <- sample.int(n=nrow(data), size=floor((k_fold-2)/k_fold*nrow(data)), replace=F)
    train_data <- data[train_sample,]
    test_valid <- data[-train_sample,]
    test_valid_sample <- sample.int(n=nrow(test_valid), size=floor(0.5*nrow(test_valid)), replace=F)
    valid <- test_valid[test_valid_sample,]
    test <- test_valid[-test_valid_sample,]
    
    split_data <- list("train"=train_data, "valid"=valid, "test"=test)
    return(split_data)
}

build_model_predict <- function(train_data, valid_test_data, accuracy_name, output_name){
    
    # declare variable
    accuracy_list <- list()
    accuracy_list <- c(accuracy_list, output_name)
    
    # build model
    model <- rpart(V2~.,
                   data=train_data, control=rpart.control(maxdepth=30),
                   method="class")
    
    index <- 1
    for(data in valid_test_data){
        
        # predict result
        resultframe <- data.frame(truth=data$V2, pred=predict(model, newdata=data, type="class"))
        
        # get accuracy
        accuracy <- round(nrow(resultframe[resultframe$truth == resultframe$pred,]) / nrow(resultframe), 2)
        accuracy_list <- c(accuracy_list, accuracy)

        # go to next 
        index <- index + 1
        
    }
    
    # map name with accuracy result
    return(accuracy_list)
}

main <- function() {
    
    # install packages
    install_packages()
    
    # get args and declare some variabled
    opt <- get_args()
    k_fold <- as.numeric(opt$fold)
    input_file <- opt$input
    output_file <- opt$output
    output_data <- list()
    row_name <- c()
    train <- c()
    valid <- c()
    test <- c()
    accuracy_name <- c("set", "train", "validation", "test")
    
    # get data
    data <- check_args(k_fold, output_file, input_file)
    
    # print status
    print_status(data, k_fold)
    
    for(k in c(1: k_fold)){
        
        cat("Processing ", k, "-", k_fold, " cross validation\n")
        
        # sample data
        split_data <- sample_train_val_test(data, k_fold)
        train_data <- split_data$train
        valid_test_data <- list(train=train_data, valid=split_data$valid, test=split_data$test)
        current_k <- as.numeric(k)
        
        # get accuracy and put in output list
        output_name <- paste("fold", as.character(k), sep="")
        row_name <- c(row_name, output_name)
        accuracy_list <- build_model_predict(train_data, valid_test_data, accuracy_name, output_name)
        output_data <- list(output_data, accuracy_list)
        
        # concate all result
        train <- c(train, accuracy_list[[2]])
        valid <- c(valid, accuracy_list[[3]])
        test <- c(test, accuracy_list[[4]])
    }
    
    # get average of train, valid, test
    # and print output
    mean_vector = c("ave.", round(mean(train), 2), round(mean(valid), 2), round(mean(test), 2))
    output_data <- list(output_data, mean_vector)
    
    # transform to data frame 
    # rbind to data frame 
    output_data <- data.frame(matrix(unlist(output_data), nrow=k_fold+1, byrow=T))
    colnames(output_data) <- accuracy_name
    cat("Output is: \n")
    print(output_data)
    
    # write csv
    write.csv(output_data,output_file, row.names = FALSE, quote = FALSE)
    cat("Save performance in", output_file)
    cat("\nFinish !")
}

main()
# x <- paste("fold", as.character(1), sep="-")
# print(x)
# output_data[[x]] <- list()
# output_data[[x]][["test"]] <- 0
# print(output_data)