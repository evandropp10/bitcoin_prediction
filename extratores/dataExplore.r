setwd("~/Projetos/Projetos_Python/tcc/extratores")

library(readr)
library(moments)
library(ggplot2)
library(ggpubr)
library(corrplot)
library(ggthemes)
library(dplyr)

dt = read_csv("data-mining.csv")

View(dt)

moda = function(data) {
  vec = table(as.vector(data))
  names(vec)[vec == max(vec)]
}

#### Analise individual da VARIAVEL BITCOIN - Expressão  "Bitcoin" Google Trends
####

x = dt$value

# Média, Mediana, Moda e Amplitude
mean(x)
median(x)
moda(x)
max(x)
min(x)
range(x)
diff(range(x))

# Quartil
quantile(x)

#Desvio Padrão
sd(x)

# Variância
var(x)

# Coeficiente de Variação
coef = (sd(x) / mean(x)) * 100
coef

# Histograma para analisar a distribuição dos dados
hist(x, main="Bitcon Google Trend Topic", xlab="Bitcoin score", breaks=10)

# Coeficiente de assimetria
skewness(x)

#Coeficiente de curtose
kurtosis(x)

# Histograma
df = data.frame(x)
ggplot(df, aes(x = x), binwidth = 2) + 
  geom_histogram(aes(y = ..density..), fill = 'red', alpha = 0.5, binwidth = 7) + 
  geom_density(colour = 'blue') + xlab(expression(bold('Dados'))) + 
  ylab(expression(bold('Densidade')))

# Boxplot
boxplot(x)

# Distribuição normal
rnorm(x)
hist(rnorm(x))

plot(x, rnorm(x), type="p")


### Correlação entre variáveis Trends: Bitcoin e Bitcoin Price
x = dt$bitcoin
y = dt$bitcoinPrice

# Coeficiente de Correlação
ggscatter(dt, x = "bitcoin", y = "bitcoinPrice",
          add = "reg.line", conf.int = TRUE, 
          cor.coef = TRUE, cor.method = "pearson",
          xlab = "Bitcoin Trends", ylab = "Bitcoin Price Trends")

# Covariância
cov(x,y)

# Correlação
cor(x,y)

### Correlação entre variáveis: Bitcoin(Trends) e value
x = dt$bitcoin
y = dt$value

# Coeficiente de Correlação
ggscatter(dt, x = "bitcoin", y = "value",
          add = "reg.line", conf.int = TRUE, 
          cor.coef = TRUE, cor.method = "pearson",
          xlab = "Bitcoin Trends", ylab = "Value")

# Covariância
cov(x,y)

# Correlação
cor(x,y)


#### ANALISANDO CORRELAÇÕES DO PREÇO
### Correlação entre variáveis: VALUE E BITCOIN
x = dt$value
y = dt$bitcoin

# Coeficiente de Correlação
ggscatter(dt, x = "value", y = "bitcoin",
          add = "reg.line", conf.int = TRUE, 
          cor.coef = TRUE, cor.method = "pearson",
          xlab = "Bitcoin Trends", ylab = "Value")

# Covariância
cov(x,y)

# Correlação
cor(x,y)

### Correlação entre variáveis: VALUE E UNIQUE
x = dt$value
y = dt$unique

# Coeficiente de Correlação
ggscatter(dt, x = "value", y = "unique",
          add = "reg.line", conf.int = TRUE, 
          cor.coef = TRUE, cor.method = "pearson",
          xlab = "Bitcoin Trends", ylab = "Bitcoin Price Trends")

# Covariância
cov(x,y)

# Correlação
cor(x,y)

### Correlação entre variáveis: VALUE E REVENUE
x = dt$value
y = dt$revenue

# Coeficiente de Correlação
ggscatter(dt, x = "value", y = "revenue",
          add = "reg.line", conf.int = TRUE, 
          cor.coef = TRUE, cor.method = "pearson",
          xlab = "Bitcoin Trends", ylab = "Bitcoin Price Trends")

# Covariância
cov(x,y)

# Correlação
cor(x,y)


## ANALISE GERAL
# Obtendo apenas as colunas numéricas
colunas_numericas <- sapply(dt, is.numeric)
colunas_numericas

# Filtrando as colunas numéricas para correlação
data_cor <- cor(dt[,colunas_numericas])
data_cor
corrplot(data_cor, method = 'color')

### ANALISANDO A VARIACAO
?plot
plot(dt$value, type='l')
lines(dt$bitcoin,  type='l', col='red')

# Correlação dos dados

