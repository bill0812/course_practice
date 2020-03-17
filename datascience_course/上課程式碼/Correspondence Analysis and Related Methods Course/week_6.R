# computing row and column contributions in CA
#   (follows on from the script of week 6)

# compute matrix of contributions for rows, and row inertias
data.rcon <- data.rpc^2 * data.r
apply(data.rcon, 1, sum)

# compute contributions and squared correlations
data.rctr <- t( t(data.rcon) / apply(data.rcon, 2, sum) )
data.rcor <- data.rcon / apply(data.rcon, 1, sum)

# compute qualities in 2-d solution
apply(data.rcor[,1:2], 1, sum)


# compute matrix of contributions for columns, and column inertias
data.ccon <- data.cpc^2 * data.c
apply(data.ccon, 1, sum)

# compute contributions and squared correlations
data.cctr <- t( t(data.ccon) / apply(data.ccon, 2, sum) )
data.ccor <- data.ccon / apply(data.ccon, 1, sum)

# compute qualities in 2-d solution
apply(data.ccor[,1:2], 1, sum)



# varying the coordinates (for example, columns) for standard biplot
# this is equivalent to map option "rowgreen" in package ca

data.cbpc <- diag(sqrt(data.c)) %*% data.csc
