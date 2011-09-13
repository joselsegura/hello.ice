public class Client extends Ice.Application {
  public int run(String[] args) {
    Ice.ObjectPrx obj = communicator().stringToProxy(args[0]);
    UCLM.HelloPrx hello = UCLM.HelloPrxHelper.checkedCast(obj);
    hello.puts("Hello, World!");
    return 0;
  }

  static public void main(String[] args) {
    Client app = new Client();
    app.main("Client", args);
  }
}
