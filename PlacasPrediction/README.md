# AwariProject
## Classificação de placas de trânsito usando Convolutional Neural Network

Este estudo tem como tema a classificação de placas de transito usando redes neurais.

O reconhecimento de sinais e placas de transito são muito utilizados em sistemas autônomos como nos carros do google ou no auxilio ao motorista como os carros Tesla.

O objetivo principal é o entendimento mais aprofundado de redes neurais convolucionais e também a aplicação de machine learning em imagens.

## Dados

Os dados foram adquiridos através do Kaggle.

Uma competição que possui placas de trânsito Alemãs e podem ser encontradas aqui:
https://www.kaggle.com/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign

![alt text](https://github.com/IvaStival/AwariProject/blob/main/plots/Final/placas.png?raw=true)

Os dados já estão divididos em treino e teste, estão devidamente catalogadas e possuem apenas imagens das placas.

São mais de 50 mil imagens e 43 tipos diferentes de placas.

## Manipulação

As imagens estão com uma ótima qualidade, porém suas dimensões são diferentes. Dessa forma foi necessário o seu redimensionamento
para o tamanho padrão de 32x32.

Também se viu necessário a equalização do contraste, pois muitas imagens são escuras.

## Bibliotecas para Modelagem

Para o treinamento e teste foi utilizado o Tensorflow/Keras. Já para a manipulação dos arquivos .cvs (Train.csv e Test.csv) foi utilizado o pandas.

Para as métricas foram salvos os históricos de cada época que o próprio modelo escolhido do Keras (Sequential) gera e também foi feita uma analise por classe no treinamento usando as metricas do sklearn (classification_report).

Já para gerar os gráficos o matplotlib e o seaborn foram os escolhidos.

## Modelo

O objectivo era alcançar o melhor resultado com um numero pequeno de épocas, no caso 30.

Para isso a proposta foi alterar alguns parametros de configuração do modelo, que são a quantidade de filtros das camadas de convolução, o tamanho desses filtros e por fim o tamanho das camadas
densas.

A rede é dividida em 3:
  - Camada de Covolução;
  - Camada Densa;
  - Camada de resultado;

E cada uma das divisões possuem suas próprias divisões.

* Camada de Convolução: Nessa camada é onde ocorre a obtenção de características das imagens e também a redução no tamanho das mesmas;

  Essa camada é divida em mais 5 camadas de convolução, sendo a primeira a camada de entrada no tamanho de 32x32.

* Camada Densa: Essa camada é a rede neural clássica, onde ocorre o aprendizado;

  Aqui com 2 camadas e o tamanho delas varia de acordo com a etapa dos testes.

* Camada de resultado: Retorna um array com a probabilidade da imagem atual ser cada uma das 43 possibilidades;

## Resultados
### Acurácia Treino e Teste
| Etapa 1 | Etapa 2 |
| :--------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------: |
| ![alt text](https://github.com/IvaStival/AwariProject/blob/main/plots/Final/Hist_Test1.png?raw=true) | ![alt text](https://github.com/IvaStival/AwariProject/blob/main/plots/Final/Hist_Test2.png?raw=true) |
| Etapa 3 | Etapa 4 |
| ![alt text](https://github.com/IvaStival/AwariProject/blob/main/plots/Final/Hist_Test3.png?raw=true) | ![alt text](https://github.com/IvaStival/AwariProject/blob/main/plots/Final/Hist_Test4.png?raw=true) |
| Etapa 5 | |
| ![alt text](https://github.com/IvaStival/AwariProject/blob/main/plots/Final/Hist_Test5.png?raw=true) |

### Todas as acurácias do treino
![alt text](https://github.com/IvaStival/AwariProject/blob/main/plots/Final/Hist_All_Train.png?raw=true)

### Todas as acurácias do test
![alt text](https://github.com/IvaStival/AwariProject/blob/main/plots/Final/Hist_All_Test.png?raw=true)

### Precisão por placa
| Etapa 1 | Etapa 2 |
| :-------------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------: |
| ![alt text](https://github.com/IvaStival/AwariProject/blob/main/plots/Final/Precision_Test1.png?raw=true) | ![alt text](https://github.com/IvaStival/AwariProject/blob/main/plots/Final/Precision_Test2.png?raw=true) |
| Etapa 3 | Etapa 4 |
| ![alt text](https://github.com/IvaStival/AwariProject/blob/main/plots/Final/Precision_Test3.png?raw=true) | ![alt text](https://github.com/IvaStival/AwariProject/blob/main/plots/Final/Precision_Test4.png?raw=true) |
| Etapa 5 | |
| ![alt text](https://github.com/IvaStival/AwariProject/blob/main/plots/Final/Precision_Test5.png?raw=true)|


Podemos notar que o melhor resultado foi a etapa numero 4, onde atingiu em media mais de 90% de acurácia tanto no treino quando no teste.
A sua configuração foi a seguinte:
  - Numero de Filtros   = 16, 32 e 64
  - Tamanho dos Filtros = 5x5 5x5 and 5x5
  - Tamanho da camada Densa = 256 e 256

Outra coisa a se notar foi o resultado da ultima etapa, que até teve um resultado ok no treino mas se perdeu totalmente no teste.
Acredito que isso se deve ao tamanho tanto da matriz quanto no numero de filtros.

Analisando os gráficos por placas vemos que a etapa número 4 é a melhor. Alcançando um boa precisão na maioria das placas.
Algumas tiveram um resultado inferior, talvez aumentando o número dessas placas ou ainda aumentar o número de épocas possa resolver.

## Trabalhos futuros
Como esse modelo apresentado consegue somente classificar imagens onde só existe a placa, um trabalho futuro é a implementação de outro modelo que consiga identificar as placas em uma imagem bruta
e assim enviar para este modelo classificar.

Outra possibilidade é a implementação em video em tempo real.

E por fim a criação de um aplicativo para uso geral.
