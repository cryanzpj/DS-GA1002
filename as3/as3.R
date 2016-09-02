
library(scatterplot3d)
library(box3d)
png(filename="/Users/cryan/Desktop/1002/as3/Q2_a.png",width = 600,height= 600)
C = 1/80000

x = c(100,300,300,0,0,100,100)
y = c(0,0,300,300,100,100,0)
z = c(C,C,C,C,C,C,C)



a = scatterplot3d(x,y,z,type = 'l',angle = 30 ,ylim = c(0,400),xlim = c(0,400),zlab = "density",xlab = "X",ylab = "R",main = 'Joint PDF of X and R',highlight.3d=TRUE ,zlim = c(0,0.00005))

for (i in 1:7){
  a$points3d(c(x[i],x[i]),c(y[i],y[i]),c(C,0),type = 'l',lty = 2)
}
par(new = T)
scatterplot3d(x,y,c(0,0,0,0,0,0,0),type = 'l',angle = 30 ,ylim = c(0,400),xlim = c(0,400),zlab = "density",xlab = "X",ylab = "R",main = 'Joint PDF of X and R',highlight.3d=TRUE ,zlim = c(0,0.00005))


dev.off()