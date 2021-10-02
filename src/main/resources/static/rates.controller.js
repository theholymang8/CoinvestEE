(function () {
    'use strict';

    angular
        .module('app')
        .controller('RatesController', RatesController );

    RatesController.$inject = ['$http'];

    function RatesController($http) {
        var vm = this;


        vm.totalBalance;
        //vm.txCheck;

        const interval = setInterval(refreshBalance, 5000);
        vm.refreshBalance = refreshBalance;
        //vm.checkTransaction = checkTransaction;
        //clearInterval(interval);

        init();

        function init(){
            refreshBalance();
        }


        function refreshBalance(){
            var url = "/dashboard/refresh";
            var refreshBalance = $http.get(url)
            refreshBalance.then(function(response){

                vm.totalBalance = response.data.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");



            });


        }


    }
})();