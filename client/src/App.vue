<template>
    <v-app>
        <v-content>
            <Header></Header>
            <keep-alive>
                <router-view />
            </keep-alive>
            <Footer></Footer>
        </v-content>
    </v-app>
</template>

<script>
import Header from '@/components/Header'
import Footer from '@/components/Footer'

export default {
    name: 'App',
    components: {
        Header,
        Footer
    }
}
</script>
