 lambda = seq(0,5,0.001)
 n = c(5,50,100)
 t1 = 0.5
 t2 = 1
 t3 = 3
 t4 = 5

 for (t1 in c(0.5,1,3,5)){
 x1 = 1 - (1 - exp(-lambda*t1))^n[1]
 x2 = 1 - (1 - exp(-lambda*t1))^n[2]
 x3 = 1 - (1 - exp(-lambda*t1))^n[3]
 png(filename=paste("/Users/cryan/Desktop/1002/as7/Q",toString(t1/0.5),".png",sep = ""),width = 600,height= 600)
 plot(lambda,x1,type = 'l',ylim = c(0,1),lty = 1,xlab = expression(lambda),ylab = expression(beta(lambda)))
 par(new = T)
 plot(lambda,x2,type = 'l',ylim = c(0,1),lty = 2,xlab = expression(lambda),ylab = expression(beta(lambda)))
 par(new = T)
 plot(lambda,x3,type = 'l',ylim = c(0,1),lty = 3,xlab = expression(lambda),ylab = expression(beta(lambda)),main = 	 paste("threshold = ", toString(t1)))
 abline(c(0.05,0),lty = 4)
 legend(4,0.9,c('n=5',"n=50","n=100"),lty = c(1,2,3))
 dev.off()
}