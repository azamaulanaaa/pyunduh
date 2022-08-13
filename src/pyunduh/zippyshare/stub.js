const document = {
    getElementById(v) {
        if (!this[v]) {
            this[v] = {}
        }
        
        return this[v]
    }
}
