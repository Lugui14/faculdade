install.packages("ggplot2")
library("ggplot2")

grafico_tendencia = ggplot(data=Orange, aes(x=age, y=circumference, color=Tree, shape=Tree))+
  geom_point(size=3)+geom_smooth(se=FALSE)+
  labs(x = 'Idade da Laranjeira', y = 'Circunferência da Laranjeira', color='Árvore', shape='Árvore')+
  ggtitle("Circunferência por idade das laranjeiras") +
  theme_minimal()

grafico_distribuicao = ggplot(data=Orange, aes(x=Tree, y=circumference, color=Tree, size=age))+
  geom_point()+
  labs(x = 'Árvore', y = 'Circunferência da laranjeira', color='Árvore', size="Idade da laranjeira")+
  ggtitle("Comparação da circunferência de cada laranjeira") +
  theme_minimal()

grafico_contorno = ggplot(data=Orange, aes(circumference, age))+
  geom_violin(scale = "area")+
  labs(x = 'Circunferência das laranjeiras', y = 'Idade das laranjeiras')+
  ggtitle("Media de circunferência da laranjeira por idade")
  theme_minimal()
