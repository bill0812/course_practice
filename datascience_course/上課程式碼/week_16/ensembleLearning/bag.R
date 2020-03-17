spamD <- read.table('spamD.tsv',header=T,sep='\t')
spamTrain <- subset(spamD,spamD$rgroup>=10)
spamTest <- subset(spamD,spamD$rgroup<10)
spamVars <- setdiff(colnames(spamD),list('rgroup','spam'))
spamFormula <- as.formula(paste('spam=="spam"',paste(spamVars,collapse=' + '),sep=' ~ '))

# Defining performance
loglikelihood <- function(y, py) {
  pysmooth <- ifelse(py==0, 1e-12,
                     ifelse(py==1, 1-1e-12, py))
  sum(y * log(pysmooth) + (1-y)*log(1 - pysmooth))
}

accuracyMeasures <- function(pred, truth, name="model") {
  dev.norm <- -2*loglikelihood(as.numeric(truth), pred)/length(pred)
  ctable <- table(truth=truth,
                  pred=(pred>0.5))
  accuracy <- sum(diag(ctable))/sum(ctable)
  precision <- ctable[2,2]/sum(ctable[,2])
  recall <- ctable[2,2]/sum(ctable[2,])
  f1 <- precision*recall
  data.frame(model=name, accuracy=accuracy, f1=f1, dev.norm)
}

# evaluating the performance of decision trees
library(rpart)
treemodel <- rpart(spamFormula, spamTrain)
accuracyMeasures(predict(treemodel, newdata=spamTrain), spamTrain$spam=="spam", name="tree,training")
accuracyMeasures(predict(treemodel, newdata=spamTest), spamTest$spam=="spam", name="tree,test")

# Bagging decision trees
ntrain <- dim(spamTrain)[1]
n <- ntrain
ntree <- 100

# Build the bootstrap samples by sampling the row indices of spamTrain with replacement.
samples <- sapply(1:ntree, FUN = function(iter) {sample(1:ntrain, size=n, replace=T)})

# Train the individual decision trees and return them in a list.
treelist <-lapply(1:ntree, FUN=function(iter) {samp <- samples[,iter]; rpart(spamFormula, spamTrain[samp,])})

# predict.bag assumes the underlying classifier returns decision probabilities, not decisions
predict.bag <- function(treelist, newdata) {
  preds <- sapply(1:length(treelist), FUN=function(iter) { predict(treelist[[iter]], newdata=newdata)})
  predsums <- rowSums(preds)
  predsums/length(treelist)
}

# Measure Bagging decision trees 
accuracyMeasures(predict.bag(treelist, newdata=spamTrain), spamTrain$spam=="spam",name="bagging, training")
accuracyMeasures(predict.bag(treelist, newdata=spamTest), spamTest$spam=="spam", name="bagging, test")

# Using random forests
library(randomForest)
set.seed(5123512)
fmodel <- randomForest(x=spamTrain[,spamVars], y=spamTrain$spam, ntree=100, nodesize=7, importance=T)
# Specify that each node of a tree must have a minimum of 7 elements, to be compatible with the default minimum node size that rpart() uses on this training set ?
accuracyMeasures(predict(fmodel, newdata=spamTrain[,spamVars],type='prob')[,'spam'], spamTrain$spam=="spam",name="random forest, train")
accuracyMeasures(predict(fmodel, newdata=spamTest[,spamVars],type='prob')[,'spam'], spamTest$spam=="spam",name="random forest, test")

# EXAMINING VARIABLE IMPORTANCE
varImp <- importance(fmodel)
head(varImp)
varImpPlot(fmodel, type=1)

# reduce the number of variables in this spam example from 57 to 25
selVars <- names(sort(varImp[,1], decreasing=T))[1:25]
fsel <- randomForest(x=spamTrain[,selVars],y=spamTrain$spam, ntree=100, nodesize=7, importance=T)
accuracyMeasures(predict(fsel, newdata=spamTrain[,selVars],type='prob')[,'spam'], spamTrain$spam=="spam",name="RF small, train")
accuracyMeasures(predict(fsel, newdata=spamTest[,selVars],type='prob')[,'spam'], spamTest$spam=="spam",name="RF small, test")


