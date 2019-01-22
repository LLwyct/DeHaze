<template>
    <v-app>
        <v-content>
            <Header></Header>
            <keep-alive>
                <router-view />
            </keep-alive>
            <Footer></Footer>
        </v-content>
        <div class="hidden-md-and-up">
            <v-navigation-drawer v-model="$store.state.drawer" absolute app temporary>
                    <v-list dense class="pt-0">
                        <v-list-tile v-for="item in items" :key="item.title" @click="linkTo(item.title)">
                            <v-list-tile-action>
                                <v-icon>{{ item.icon }}</v-icon>
                            </v-list-tile-action>
                            <v-list-tile-content>
                                <v-list-tile-title>{{ item.title }}</v-list-tile-title>
                            </v-list-tile-content>
                        </v-list-tile>
                    </v-list>
            </v-navigation-drawer>
        </div>
    </v-app>
</template>

<script>
import Header from '@/components/Header'
import Footer from '@/components/Footer'

export default {
    name: 'App',
    data () {
        return {
            items: [
                {
                    title: 'home',
                    icon: 'dashboard'
                },
                {
                    title: 'about',
                    icon: 'question_answer'
                },
                {
                    title: 'fix',
                    icon: 'dashboard'
                }
            ]
        }
    },
    components: {
        Header,
        Footer
    },
    methods: {
        linkTo (title) {
            this.$router.replace({
                name: title
            })
        }
    }
}
</script>
