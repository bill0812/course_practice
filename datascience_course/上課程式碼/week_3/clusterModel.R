
#Clustering random data in the plane
set.seed(32297)
d <- data.frame(x=runif(100),y=runif(100))
clus <- kmeans(d,centers=5)
d$cluster <- clus$cluster

#Calculating the size of each cluster
table(d$cluster)

#Calculating the typical distance between items in every pair of clusters
library('reshape2')
n <- dim(d)[[1]]
pairs <- data.frame(
   ca = as.vector(outer(1:n,1:n,function(a,b) d[a,'cluster'])),
   cb = as.vector(outer(1:n,1:n,function(a,b) d[b,'cluster'])),
   dist = as.vector(outer(1:n,1:n,function(a,b)
           sqrt((d[a,'x']-d[b,'x'])^2 + (d[a,'y']-d[b,'y'])^2)))
   )
dcast(pairs,ca~cb,value.var='dist',mean)
