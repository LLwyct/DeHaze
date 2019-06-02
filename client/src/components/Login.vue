<template>
    <v-container>
        <h1 style="margin: 0 0 20px 0" id="title">login</h1>
        <div class="loginbox" id="loginbox">
            <input type="text" v-model="username">
            <input type="password" v-model="password">
            <button @click="Login">GO!</button>
        </div>
        <div id="filebox">

        </div>
    </v-container>
</template>
<script>
import AuthService from '@/services/authService.js';
export default {
    data () {
        return {
            username: '',
            password: ''
        }
    },
    methods: {
        async Login () {
            // console.log(this.username, this.password);
            let result = await AuthService.checkAuth({
                username: this.username,
                password: this.password
            });
            try {
                const filelist = result.data.filenamelist;
                document.getElementById('loginbox').style.display = 'none';
                document.getElementById('title').innerText = 'file list';
                JSON.parse(filelist).forEach(element => {
                    let filename = document.createElement('h3');
                    filename.innerText = element;
                    document.getElementById('filebox').appendChild(filename);
                });
                document.getElementById('filebox').style.display = 'block';
            } catch (error) {
                console.error(error);
            }
            console.log(result);
        }
    }
}
</script>

<style scoped>
.loginbox {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
}
.loginbox input {
    width: 100%;
    font-size: 1.4em;
    box-sizing: border-box;
    background: #ececec;
    border-radius: 5px;
    margin-bottom: 20px;
    padding: 10px 15px;
    outline: none;
}
.loginbox input:focus {
    background: gainsboro;
}
.loginbox button {
    width: 20%;
    min-width: 100px;
    outline: none;
    border: 2px solid;
    border-radius: 3px;
    height: 40px;
    font-size: 1.5em;
    font-weight: bold;
    transition: 50ms linear;
}
.loginbox button:hover {
    font-size: 1.7em;
}
#filebox {
    display: none;
    border-top: 1px solid #e3e3e3;
}
</style>
