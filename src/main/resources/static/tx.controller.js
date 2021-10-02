
var app = angular.module("tx", []);

app.controller("txController", function($scope){
    $scope.submitHandler = function(txAction, txNumber, txCoin){


        then(function(response){
            $scope.result = response.data.toString();
                if($scope.result=="true"){
                    window.alert("Transaction Completed Succsefully!");
                }else{
                    window.alert("Transaction Failed");
                }
                //window.alert($scope.result);

                //window.alert("Tx Failed!")

        });
    }
})