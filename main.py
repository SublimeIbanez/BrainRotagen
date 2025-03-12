import tk_async_execute
import application 

if __name__ == "__main__":
    app = application.Application()
    tk_async_execute.start()
    app.run()
    tk_async_execute.stop()