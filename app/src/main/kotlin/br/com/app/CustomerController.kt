package br.com.app
import org.springframework.http.ResponseEntity
import org.springframework.web.bind.annotation.PostMapping
import org.springframework.web.bind.annotation.RequestBody
import org.springframework.web.bind.annotation.RestController

@RestController
class CustomerController(
    private val customerService: CustomerService
) {
    @PostMapping("/customer")
    fun createNewCustomer(@RequestBody customer: Customer): ResponseEntity<String> {
        val response = customerService.createNewCustomer(customer)
        return ResponseEntity.status((response!!.statusCode())).body(response.body())
                }
}