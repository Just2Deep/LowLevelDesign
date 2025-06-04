from adapter import XMLProviderAdapter
from xml_provider import XMLDataProvider
from reports import IReport


class Client:
    def __init__(self, adapter: IReport):
        self.adapter = adapter

    def get_report(self):
        return self.adapter.get_json_data()

    def run(self):
        result = self.get_report()
        print(f"Client received: {result}")


if __name__ == "__main__":
    xml_data = "<root><element>Value</element></root>"
    xml_provider = XMLDataProvider(xml_data)
    adapter = XMLProviderAdapter(xml_provider)
    client = Client(adapter)
    client.run()
