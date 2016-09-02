
p = function(N,K,C){
	if (C == 0.25){
		1/30 * choose(N,K) * (C)^K * (1-C)^(N-K)
	}
	else{
		1/60 * choose(N,K) * (C)^K * (1-C)^(N-K)

	}
		
} 

cdf = function(K,C){
	N = seq(0,20)
	pmf = p(N,K,C)/ sum(p(N,K,C))
	res = c()
	for (i in 0:20){
		res[length(res)+1] = sum(pmf[1:(i+1)])	
	
	}
	res
}

K1_0.25 = cdf(1,0.25)
K10_0.25 = cdf(10,0.25)
K19_0.25 = cdf(19,0.25)

K1_0.8 = cdf(1,0.8)
K10_0.8 = cdf(10,0.8)
K19_0.8 = cdf(19,0.8)

png(filename="/Users/cryan/Desktop/1002/as4/Q2_d_1.png",width = 600,height= 600)

plot(c(0:20),K1_0.25,type = 'o',pch = 1,cex= 0.7,ylab = 'CDF',xlab = 'N',main = 'Distribution of N,C = 0.25')
par(new = T)
plot(c(0:20),K10_0.25,type = 'o',pch = 1,cex= 0.7,ylab = 'CDF',xlab = 'N')
par(new = T)
plot(c(0:20),K19_0.25,type = 'o',pch = 1,cex= 0.7,ylab = 'CDF',xlab = 'N')
text(16,0.2,'K=10');text(10,0.7,"K = 1");text(20,0.1,"K = 19",cex = 0.8)
dev.off()

png(filename="/Users/cryan/Desktop/1002/as4/Q2_d_2.png",width = 600,height= 600)
plot(c(0:20),K1_0.8,type = 'o',pch = 1,cex= 0.7,ylab = 'CDF',xlab = 'N',main = 'Distribution of N,C = 0.8')
par(new = T)
plot(c(0:20),K10_0.8,type = 'o',pch = 1,cex= 0.7,ylab = 'CDF',xlab = 'N')
par(new = T)
plot(c(0:20),K19_0.8,type = 'o',pch = 1,cex= 0.7,ylab = 'CDF',xlab = 'N')
text(11,0.6,'K=10');text(5,0.9,'K=1');text(17,0.2,'K=19')
dev.off()





