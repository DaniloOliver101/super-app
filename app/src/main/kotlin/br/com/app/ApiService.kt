package br.com.app

import org.springframework.beans.factory.annotation.Value
import org.springframework.stereotype.Service
import java.net.URI
import java.net.http.HttpClient
import java.net.http.HttpRequest
import java.net.http.HttpRequest.BodyPublishers
import java.net.http.HttpResponse
import java.net.http.HttpResponse.BodyHandlers

@Service
class ApiService {
    @Value("\${api.host}")
    private lateinit var host: String

    val client = HttpClient.newHttpClient()

    fun postCustomer(customer: Customer) {

    }

    fun <T> post(data: T): HttpResponse<String>? {
        val json = data.toString()

        val request = HttpRequest.newBuilder()
            .uri(URI.create(host))
            .POST(BodyPublishers.ofString(json))
            .header("Content-Type", "application/json")
            .build()

        return client.send(request, BodyHandlers.ofString())
    }

    fun get(apiUrl: String): HttpResponse<String>? {
        val request = HttpRequest.newBuilder()
            .uri(URI.create(apiUrl))
            .GET()
            .build()

        return client.send(request, BodyHandlers.ofString())
    }

    fun <T> put(apiUrl: String, data: T): HttpResponse<String>? {
        val json = data.toString()

        val request = HttpRequest.newBuilder()
            .uri(URI.create(apiUrl))
            .PUT(BodyPublishers.ofString(json))
            .header("Content-Type", "application/json")
            .build()

        return client.send(request, BodyHandlers.ofString())
    }

    fun <T> patch(apiUrl: String, data: T): HttpResponse<String>? {
        val json = data.toString()

        val request = HttpRequest.newBuilder()
            .uri(URI.create(apiUrl))
            .method("PATCH", BodyPublishers.ofString(json))
            .header("Content-Type", "application/json")
            .build()

        return client.send(request, BodyHandlers.ofString())
    }

    fun delete(apiUrl: String): HttpResponse<String>? {
        val request = HttpRequest.newBuilder()
            .uri(URI.create(apiUrl))
            .DELETE()
            .build()

        return client.send(request, BodyHandlers.ofString())
    }
}