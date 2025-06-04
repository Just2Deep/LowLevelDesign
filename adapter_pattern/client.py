from adapter import XMLProviderAdapter
from xml_provider import XMLDataProvider
from reports import IReport


class Client:
    def get_report(self, adapter: IReport, base_data: str = ""):
        return adapter.get_json_data(base_data)

    def run(self, adapter: IReport, base_data: str = ""):
        result = self.get_report(adapter, base_data)
        print(f"Client received: {result}")


if __name__ == "__main__":
    xml_data = "<root><element>Value</element></root>"
    xml_provider = XMLDataProvider()
    adapter = XMLProviderAdapter(xml_provider)
    client = Client()
    client.run(adapter, xml_data)
