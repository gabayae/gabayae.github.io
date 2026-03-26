# Chapter 9: Introduction to R for Statistics

# === Vectors ===
heights <- c(170, 165, 180, 175, 168, 172, 178, 163, 185, 171)
cat("Heights:", heights, "\n")
cat("Mean:", mean(heights), "\n")
cat("SD:", sd(heights), "\n")
cat("Median:", median(heights), "\n")

# === Summary ===
cat("\nSummary:\n")
print(summary(heights))

# === t-test ===
group_a <- c(85, 90, 78, 92, 88, 76, 95, 89)
group_b <- c(78, 82, 75, 80, 85, 70, 88, 79)
result <- t.test(group_a, group_b)
cat("\nt-test:\n")
print(result)

# === Correlation ===
x <- c(1, 2, 3, 4, 5, 6, 7, 8)
y <- c(2.1, 4.0, 5.8, 8.2, 9.9, 12.1, 14.0, 16.1)
cat("\nCorrelation:", cor(x, y), "\n")

# === Linear regression ===
model <- lm(y ~ x)
cat("\nLinear Regression:\n")
print(summary(model))

# === Plots ===
pdf("ch09_histogram.pdf")
hist(heights, breaks=6, col="steelblue", main="Height Distribution",
     xlab="Height (cm)", ylab="Frequency")
dev.off()

pdf("ch09_scatter.pdf")
plot(x, y, pch=19, col="blue", main="Scatter Plot",
     xlab="x", ylab="y")
abline(model, col="red", lwd=2)
dev.off()

cat("\nPlots saved.\n")
