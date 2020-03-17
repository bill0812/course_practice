# read in data into data-frame data_set

# the next 14 commands are all you need to compute CA results

data.P<-data/sum(data_set)
data.r<-apply(data.P,1,sum)
data.c<-apply(data.P,2,sum)
data.Dr<-diag(data.r)
data.Dc<-diag(data.c)
data.Drmh<-diag(1/sqrt(data.r))
data.Dcmh<-diag(1/sqrt(data.c))

data.P<-as.matrix(data.P)
data.S<-data.Drmh%*%(data.P-data.r%o%data.c)%*%data.Dcmh
data.svd<-svd(data.S)

data.rsc<-data.Drmh%*%data.svd$u
data.csc<-data.Dcmh%*%data.svd$v
data.rpc<-data.rsc%*%diag(data.svd$d)
data.cpc<-data.csc%*%diag(data.svd$d)

# the symmetric map

plot(data.rpc[,1],data.rpc[,2],type="n",pty="s")
text(data.rpc[,1],data.rpc[,2],label=rownames(data))

# rescaling the optimal scale

data.range<-max(data.csc[,1])-min(data.csc[,1])
data.scale<-(data.csc[,1]-min(data.csc[,1]))*100/data.range

# now do it in one shot using ca package (first install from CRAN)
library(ca)
plot(ca(data_set))

