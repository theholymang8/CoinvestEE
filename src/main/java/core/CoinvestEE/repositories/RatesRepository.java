package core.CoinvestEE.repositories;

import core.CoinvestEE.model.Rates;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by Giannis Anastasopoulos on 20/05/21
 */

public interface RatesRepository extends CrudRepository<Rates, Long> {
    @Query(value = "SELECT ada_rate FROM Rates WHERE rateid=(SELECT max(rateid) FROM Rates);",
    nativeQuery = true)
    Double findLatestAdaRate();
    @Query(value = "SELECT bitcoin_rate FROM Rates WHERE rateid=(SELECT max(rateid) FROM Rates);",
            nativeQuery = true)
    Double findLatestBtcRate();
    @Query(value = "SELECT ethereum_rate FROM Rates WHERE rateid=(SELECT max(rateid) FROM Rates);",
            nativeQuery = true)
    Double findLatestEthRate();
    @Query(value = "SELECT monero_rate FROM Rates WHERE rateid=(SELECT max(rateid) FROM Rates);",
            nativeQuery = true)
    Double findLatestXmrRate();

}
