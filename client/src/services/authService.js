import Api from '@/services/API'

export default {
    checkAuth (userinfo) {
        return Api().post('dehaze/auth', userinfo)
    }
}