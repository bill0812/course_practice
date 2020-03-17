## STA254 Correspondence Analysis and Related Methods
## Michael Greenacre

## Week2                                             
## Multidimensional scaling (MDS), Classical scaling

#  This script continues from week 1's script on distances
#  where we computed the dissimilarity matrix BC and 
#  distance matrix chid

# MULTIDIMENSIONAL SCALING
# Computing step 8
# Classical Multidimensional scaling (MDS)

# First we do the simple classroom example "by hand"

d2   <- matrix(c(0,17,17,16,17,0,4,41,17,4,0,25,16,41,25,0),nrow=4)

n    <- nrow(d2)
ones <- rep(1,n)
I    <- diag(ones)
Sd   <- -0.5*(I - (1/n) * ones %*% t(ones)) %*% d2 %*% (I - (1/n) * ones %*% t(ones))

Sd.eig <- eigen(Sd)

X    <- Sd.eig$vectors[,1:2] %*% diag(sqrt(Sd.eig$values[1:2]))
plot(X, type="n")
text(X, labels=1:4)

# verify that distances are recovered
dist(X)^2

# use R function cmdscale

plot(cmdscale(sqrt(d2)), type="n")
text(cmdscale(sqrt(d2)), labels=1:4)



# Computing step 9

# assuming Bray-Curtis dissimilarities are in BC
# (can be matrix or distance object in this case)

MDS.BC <- cmdscale(BC, eig=T) 	# calculate classical MDS

# see what's in the object

names(MDS.BC)

MDS.BC <- cmdscale(BC, eig=T, k=29)

# (don't worry about warning message about negative eigenvalues)


# assuming chi-square distances are in chid

MDS.chi <- cmdscale(chid, eig=T, k=29)


# Computing step 10
# check the eigenvalues and plot the points (dots)

MDS.BC$eig			# eigenvalues from MDS based on Bray-Curtis
MDS.chi$eig			# eigenvalues from MDS based on chi-square distance

plot(MDS.BC$points[,1], MDS.BC$points[,2])

# plot the points (sequence numbers)
plot(MDS.BC$points[,1], MDS.BC$points[,2], type="n")
text(MDS.BC$points[,1], MDS.BC$points[,2])

# plot the points (labels)
plot(MDS.BC$points[,1], MDS.BC$points[,2], type="n")
lab.s<-labels(data)[[1]]
text(MDS.BC$points[,1], MDS.BC$points[,2], labels=lab.s)


# Computing step 11
# Nonmetric Multidimensional scaling (MDS)
library(MASS) 			# load library 'MASS' to access function isoMDS()
nMDS.BC<-isoMDS(BC)		# calculate nonmetric MDS

# plot the points (labels)
plot(nMDS.BC$points[,1], nMDS.BC$points[,2], type="n")
lab.s<-labels(data)[[1]]
text(nMDS.BC$points[,1], nMDS.BC$points[,2], labels=lab.s)
