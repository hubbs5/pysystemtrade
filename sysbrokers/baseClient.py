
class brokerClient(object):
    """

    Broker server classes are called by the brokers server application (eg IB Gateway)

    We inherit from this for specific brokers and over ride the methods in the base class to ensure a consistent API

    """

    """
    Following two methods implement context manager
    """
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_connection()


    def broker_get_daily_fx_data(self, ccy1, ccy2="USD"):
        raise NotImplementedError

    def broker_get_futures_contract_list(self, instrument_object_with_broker_config):
        raise NotImplementedError

    def broker_get_historical_futures_data_for_contract(self, contract_object_with_broker_config):
        raise NotImplementedError

    def broker_get_contract_expiry_date(self, contract_object_with_ib_broker_config):
        raise NotImplementedError

    def close_connection(self):
        pass