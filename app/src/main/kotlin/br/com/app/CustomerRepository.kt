package br.com.app

import org.springframework.data.mongodb.repository.MongoRepository
import org.springframework.stereotype.Repository

@Repository 
interface CustomerRepository : MongoRepository<Customer, String>