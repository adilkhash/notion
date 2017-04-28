var app = new Vue({
    el: '#app',
    data: {
        email: '',
        subscribed: false,
        invalidSubscription: false,
        validationError: ''
    },
    methods: {
        subscribeBtn: function (e) {
            this.invalidSubscription = false;
            this.subscribed = false;
            this.validationError = '';

            axios.post('/subscribe/', Qs.stringify({'email': this.email}))
                .then(function (response) {
                    if (response.data.status == 'ok') {
                        app.subscribed = true;
                        app.email = '';
                    } else {
                        app.invalidSubscription = true;
                        app.validationError = response.data.msg;
                    }
                })
                .catch(function (error) {
                    app.invalidSubscription = true;
                })
        }
    }
});
