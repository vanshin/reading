var template = 
'<div id="test">' +
    '<div class="ui vertical following fluid accordion text menu">' + 
        '<template v-for="(item, index) in items">' +
            '<div class="title">' +
                '<i class="dropdown icon"></i>' +
                '<b>{{index}}</b>' +
            '</div>' +
            '<div class="content">' +
                '<div class="ui list">' +
                    '<a class="item reading-list" v-for="(li, index) in item" :id="index">' +
                        '{{li}}' +
                    '</a>' +
                '</div>' +
            '</div>' +
        '</template>' +
    '</div>' +
'</div>'

Vue.component(
    'accordion', {
        template: template,
        props: ['items']
    }
)

new Vue({
    el: '#sidebar',
    data: {
        items: '',
    },
    mounted: function(){
        var _self = this;
        axios.get('current_user/id')
            .then(function (response){
                var id = response.data.id
                axios.get('/user/'+ id +'/list',)
                    .then(function (response){
                        var list = response.data
                        delete list.message
                        delete list.code
                        _self.items = list
                    })
            })
    },
    methods: {

    }
})



$('.ui.accordion')
  .accordion()
;