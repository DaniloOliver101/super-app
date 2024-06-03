package br.com.app

import org.springframework.data.annotation.Id
import org.springframework.data.mongodb.core.mapping.Document

@Document(collection = "customers")
class Customer(
    @Id
    var id: String? = null,
    var nome: String,
    var cpf: String,
    var email: String,
    var status: CustomerStatus = CustomerStatus.ACTIVE

)

enum class CustomerStatus {
    ACTIVE, INACTIVE
}