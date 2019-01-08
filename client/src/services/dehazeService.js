import Api from '@/services/API'

export default {
    dehaze (file) {
        return Api().post('dehaze/', file)
    }
}