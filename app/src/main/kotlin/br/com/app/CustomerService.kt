package br.com.app

import org.slf4j.Logger
import org.slf4j.LoggerFactory
import org.springframework.stereotype.Service
import java.net.http.HttpResponse

@Service
class CustomerService(
    private val customerRepository: CustomerRepository,
    private val apiService: ApiService,


    ) {
    private val logger: Logger = LoggerFactory.getLogger(CustomerService::class.java)

    fun createNewCustomer(customer: Customer): HttpResponse<String>? {
        logger.info(("iniciando cadastro de cliente"))
        return apiService.post(("http://localhost:5000/customer"), buildCustomerObject((customer)))


    }

    fun buildCustomerObject(customer: Customer): String {
        return """
            {
                "cpf": "${customer.cpf}",
                "nome": "${customer.nome}",
                "email": "${customer.email}"
            }
        """.trimIndent()

    }
}