## STA254 Correspondence Analysis and Related Methods
## Michael Greenacre

## Week 4                                             
## Principal component analysis

# This script continues previous ones, and assumes that we have the 
# "abcde" species data in data frame abcde, and the three environmental
# variables in x, y and z, as well as their standardized forms in 
# xst, yst and zst (see script for Week 1; revise also Computing step 12 
# in week 3)

# PRINCIPAL COMPONENT ANALYSIS
# Computing step 15

# First, let's do the whole thing "by hand", using the three environmental 
# variables x, y and z from BioEnvGeo.
# Since the weights are equal for each of the 30 sites, we won't set 
# up the diagonal matrix D_r and its inverse, we just use scaling factors 1/n 
# and n for these

# (uppercase) X denotes original matrix X from the notes, 
# (uppercase) Y denotes column centered X

# replace the next statement according to application

X <- BioEnvGeo[,6:8]

n <- nrow(X)
p <- ncol(X)
Y <- sweep(X, 2, apply(X,2,mean))
 
# s2 contains the column variances BUT dividing by n not by n-1 in the computation
# hence the premultiplication by (n-1)/n

s2    <- ((n-1)/n)*apply(X, 2, var)

# Dsm1 is the inverse square root of these variances (i.e. std devns) in a diagonal matrix

Dsm1  <- diag(1/sqrt(s2))

# S is the matrix for svd-ing

S     <- sqrt(1/n) * as.matrix(Y) %*% Dsm1

S.svd <- svd(S)

# the row coordinates and their plotting

FF    <- sqrt(n) * S.svd$u %*% diag(S.svd$d) 

plot(FF[,1], FF[,2], type="n", xlab="PCA axis 1", ylab="PCA axis 2", main="PCA biplot")
text(FF[,1], FF[,2], labels=rownames(X), col="blue", font=2)

# adding principal axes as gray dashed lines
abline(h=0, lty=2, col="gray")
abline(v=0, lty=2, col="gray")


#------------------------------------------------------------------
# Computing step 16

# look at correlations between "old" variables in S and "new" variables in FF
# loads is between-set loadings matrix

cor(cbind(S,FF))

loads <- cor(cbind(S,FF))[1:p,(p+1):(2*p)]

# (row sum of squares of loadings is 1; column sum of squares is variance explained per axis)

apply(loads^2, 1, sum)
apply(loads^2, 2, sum)


# add biplot vectors as red arrows, either by regression or by correlation
# (since the principal axes are orthonormal, it doesn't matter which way, so we 
# use the correlation coefficients in loads)

for(j in 1:p) {
  arrows(0,0,loads[j,1], loads[j,2], length=0.1, angle=15, col="red", lwd=2)
  text(1.1*loads[j,1],1.1*loads[j,2], labels=colnames(X)[j], col="red")
  }

# how much variance of each variable explained in two-dimensions

apply(loads[,1:2]^2, 1, sum)


#------------------------------------------------------------------
# Computing step 17

# Use prcomp or princomp to do PCA

# in function princomp, the option cor=T implies standardization of variables (columns)
biplot(princomp(X, cor=T), scale=0)

# in function prcomp, the option scale=T implies standardization of variables (columns)
biplot(prcomp(X, scale=T), scale=0)

# in the above, the biplot function has option scale=alpha,where
#     alpha=1 if singular values go with variables (column principal coordinates, rows standard)
#     alpha=0 if singular values go with cases (row principal coordinates, columns standard)





