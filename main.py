if __name__ == "__main__":
    from tests.Services.MLOneWorkServices import MLOneWorkServices
    model = MLOneWorkServices.http_request()
    print(model)