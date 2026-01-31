FROM eclipse-temurin:11-jre
COPY target/demoapp-1.0-SNAPSHOT.jar app.jar
ENTRYPOINT ["java","-jar","/app.jar"]

