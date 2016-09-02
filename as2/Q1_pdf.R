png(filename="/Users/cryan/Desktop/LaTex/as2/Q1_pdf.png",width = 600,height= 600)


plot(c(0,6),c(10/288,10/288),type = "l",ylim  = c(0,1),xlim =c(0,10),main = "PDF Plot of Height",xlab= 'y',ylab = 'P')
points(c(6,6),c(10/288,13/36),type = "l",pch = 4,lty = 3)
points(c(6,8),c(13/36,13/36),type = "l",pch = 4)
points(c(8,8),c(13/36,10/288),type = "l",pch = 4,lty = 3)
points(c(8,10),c(10/288,10/288),type = "l",pch = 4)
points(6,10/288,type = 'p',cex = 1)
points(8,13/36,type = 'p',cex = 1)
dev.off()



png(filename="/Users/cryan/Desktop/LaTex/as2/Q1_2.png",width = 600,height= 600)
plot(c(0,6),c(0,180/288),type = "l",ylim  = c(0,1),xlim =c(0,10),main = "Condition CDF Plot of Height",xlab= 'y',ylab = 'P')
points(c(6,8),c(180/288,228/288),type = "l",pch = 4)
points(c(8,10),c(228/288,1),type = "l",pch = 4)
dev.off()

x = seq(0,5,0.001)
y1 = 1-exp(-2*x)
y2 = 1+ exp(-2*x) -2*exp(-x)
y3 = 1 - exp(-x)
png(filename = '/Users/cryan/Desktop/LaTex/as2/Q2_3.png',width = 600,height = 600)
plot(x,y1,type = 'l',col = 'red',ylim = c(0,1),ylab = 'CDF',main = "CDF Plots")
text(c(1,2),expression(T[1]),col = 'red')
par(new = T)
plot(x,y2,type = 'l',ylim = c(0,1),ylab = 'CDF')
text(c(3,0.5),expression(T[2]),col = 'black')
par(new = T)
plot(x,y3,type = 'l',ylim = c(0,1),ylab = 'CDF',col = 'blue')
text(1,0.7,expression(T[3]),col = 'blue')
dev.off()

png(filename="/Users/cryan/Desktop/LaTex/as2/Q4_1.png",width = 600,height= 600)
plot(c(0,0,10,10,0),c(0,10,10,0,0),type  = 'l',ylab = 'Hannah',xlab = 'Mary',ylim = c(0,12),xlim = c(0,12),main = "Joint PDF of Marry and Hannah")
x = c(0,0,10,10,0)
y= c(0,10,10,0,0)
polygon(x,y,col =gray(0.8))
text(6,11,'f = 1/100 inside the square (includig closure)')
dev.off()

png(filename="/Users/cryan/Desktop/LaTex/as2/Q4_2.png",width = 600,height= 600)
plot(c(0,0,10,10,0),c(0,10,10,0,0),type  = 'l',ylab = 'Hannah',xlab = 'Mary',ylim = c(0,12),xlim = c(0,12),main = "Joint PDF of Marry and Hannah")
points(c(0,6),c(4,10),type = 'l')
points(c(4,10),c(0,6),type = 'l')
x = c(0,6,10,10,4,0)
y = c(4,10,10,6,0,0)
polygon(x,y,col =gray(0.8))
text(2,7,'x-y = d')
text(8,3,'x-y = -d')
dev.off()

png(filename="/Users/cryan/Desktop/LaTex/as2/Q4_3.png",width = 600,height= 600)
x = seq(0,10,0.001)
y = (20-2*x)/100
plot(x,y,type  = 'l',ylab = 'PDF',xlab = 'Distance',ylim = c(0,0.4),xlim = c(0,10),main = "CDF of Distance")
dev.off()

x = seq(0.5,1,0.0001)
y1 = 8/6 * x^2 -1/3 
y2 = 8*x -4*x^2 -3

#for (i in 1:5){
#	y_1 = cbind(y_1, 1/(1- 0.5^(i+2)) *(x^(i+2) - 0.5^(i+2)))
#	y_2 = cbind(y_2, (-1)^(i+1)*((2-2*x)^(i+2) -1 ))
#	
#}



png(filename="/Users/cryan/Desktop/LaTex/as2/Q5_2.png",width = 600,height= 600)
plot(x,y1,type = 'l',col = 'red',xlab = 'bias',ylim = c(0,1),ylab = 'CDF',main = "Posterior CDF Plot of bias After The First Flip",xlim = c(0.5,1))
text(0.9,0.4,'posterior of bias given Heads',col = 'red')
par(new = T)
plot(x,y2,type = 'l',ylim = c(0,1),ylab = 'CDF',xlab = "bias")
text(c(3,0.5),expression(T[2]),col = 'black')
text(0.65,0.8,'posterior of bias given tail',col = 'black')
dev.off()

