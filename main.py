from db import ConnnectMongoDb

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    db_ins = ConnnectMongoDb()
    # db_ins.insert(
    #     {"event_name": 'su',
    #      'event_params': [{
    #          'offer_amount': 10,
    #          'min_offer_size': 100,
    #          'free_shipping': False
    #      }]}
    # )


    collection_data = db_ins.find(data={"event_name": 'su'})
    for i in collection_data:
        print(i)
