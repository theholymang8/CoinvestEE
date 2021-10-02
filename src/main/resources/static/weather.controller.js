(function () {
    'use strict';

    angular
        .module('app')
        .controller('WeatherController', WeatherController );

    WeatherController.$inject = ['$http'];

    function WeatherController($http) {
        var vm = this;


        vm.weatherStats;
        //vm.txCheck;

        const interval = setInterval(refreshTemp, 50000);
        vm.refreshTemp = refreshTemp;
        //vm.checkTransaction = checkTransaction;
        //clearInterval(interval);

        init();

        function init(){
            refreshTemp();
        }



        function refreshTemp(){
            var url = "http://api.openweathermap.org/data/2.5/weather?q=Athens&units=metric&appid=920ec499d78d5b7917027e04f201c67b";
            var refreshTemp = $http.get(url)
            refreshTemp.then(function(response){

                vm.weatherStats= response.data;


            });


        }


    }
})();