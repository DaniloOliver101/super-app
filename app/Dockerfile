# Definir a imagem base
FROM openjdk:17-jdk-alpine

# Definir a variável de ambiente para o diretório de trabalho
ENV APP_HOME=/usr/app/

# Criar o diretório de trabalho
RUN mkdir $APP_HOME

# Definir o diretório de trabalho
WORKDIR $APP_HOME

# Copiar o arquivo .jar para a imagem
COPY target/app-0.0.1-SNAPSHOT.jar $APP_HOME

# Definir o comando para iniciar o aplicativo
CMD ["java", "-jar", "app-0.0.1-SNAPSHOT.jar"]