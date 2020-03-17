## STA254 Correspondence Analysis and Related Methods
## Michael Greenacre

## Week 3                                             
## Regression biplots; dimension reduction

# This script continues previous ones, and assumes that we have the 
# "abcde" species data in data frame abcde, and the three environmental
# variables in x, y and z, as well as their standardized forms in 
# xst, yst and zst (see script for Week 1)

# REGRESSION BIPLOTS
# Computing step 12

# To find the direction vector for (species) variable "d" in the scatterplot
# of the standardized variables pollution and depth

# NOTE: we have called the 3 environmental variables Pollution, Depth and 
# Temperature x, y and z here, but in the class notes I use y for Pollution
# and x for Depth.  This can be confusing, so beware of it!
# In the script below, I have reversed the roles of "x" and "y" accordingly
# so that the plots come out as in the class notes, i.e. I use yst for the 
# horizontal axis, and xst for the vertical axis

# Do the basic scatterplot of the cases

plot(yst,xst,xlab="standardized depth", ylab="standardized pollution", type="n")
text(yst,xst,labels=rownames(BioEnvGeo))

# Standardize "d", and do the multiple regression on yst and xst

d   <- abcde[,4]
dst <- (d-mean(d))/sd(d)
reg_dxy <- lm(dst~yst+xst)

# Check out the contents of the object reg_dxy using names(reg_dxy)

# Add an arrow according to the regression coefficients

arrows(0,0,reg_vxy$coefficients[2],reg_vxy$coefficients[3], col="red")
text(1.1*reg_vxy$coefficients[2],1.1*reg_vxy$coefficients[3], labels=colnames(BioEnvGeo)[j], col=j)


# Computing step 13
# Do the same thing for all five variables (columns of abcde)
# This illustrates a for loop in R

plot(yst,xst,xlab="standardized depth", ylab="standardized pollution", type="n")
text(yst,xst,labels=rownames(BioEnvGeo))

for(j in 1:5) {
  v <- BioEnvGeo[,j]
  vst <- (v-mean(v))/sd(v)
  reg_vxy <- lm(vst~yst+xst)
  arrows(0,0,reg_vxy$coefficients[2],reg_vxy$coefficients[3], col="red")
  text(1.1*reg_vxy$coefficients[2],1.1*reg_vxy$coefficients[3], labels=colnames(BioEnvGeo)[j], col="red")
  }

# Look at the options for function arrows and try to make better looking arrows



# DIMENSION REDUCTION: 
# SINGULAR VALUE DECOMPOSITION (SVD) & PRINCIPAL COMPONENT ANALYSIS (PCA)


# Computing step 14

# first read in E.U. economic indicators into data.frame EU

n  <- nrow(EU)
p  <- ncol(EU)

# Dr is the diagonal matrix of row weights, each equal to 1/12
# Drm1 is the inverse of Dr

Dr    <- diag(rep(1, n)/n)
Drm1  <- diag(rep(n,n))

# The sweep operator subtracts (by default) out rows (1) or columns (2), functioning 
# similar to apply operator.  So this command centers the rows by the 

Y     <- sweep(EU, 2, apply(EU, 2, mean))

# s2 contains the column variances BUT dividing by n not by n-1 in the computation
# hence the premultiplication by (n-1)/n

s2    <- ((n-1)/n)*apply(EU, 2, var)

# Dsm1 is the inverse square root of the variances (i.e. std devns) in a diagonal matrix,

Dsm1  <- diag(1/sqrt(s2))

# S is the matrix for svd-ing

S     <- sqrt(Dr) %*% as.matrix(Y) %*% Dsm1

S.svd <- svd(S)

# here come the row coordinates and their plotting

FF    <- sqrt(Drm1) %*% S.svd$u %*% diag(S.svd$d) 

plot(FF[,1], FF[,2], type="n")
text(FF[,1], FF[,2], labels=rownames(EU))



