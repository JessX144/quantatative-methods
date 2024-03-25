// FooBar class is passed to 2 different threads, how do we output "FooBar" n number of times?
class FooBar {
    private int n;

    // Flag allowing threads to wait for release until executing.
    // Initialised with number of permits - acquire() removes a permit, release() adds one.
    // Doesn't execute until has a permit
    private Semaphore semaphore = new Semaphore(1);
    private Semaphore semaphore2 = new Semaphore(0);

    public FooBar(int n) {
        this.n = n;
    }

    public void foo(Runnable printFoo) throws InterruptedException {

        for (int i = 0; i < n; i++) {
            semaphore.acquire();
            printFoo.run();
            semaphore2.release();
        }
    }

    public void bar(Runnable printBar) throws InterruptedException {

        for (int i = 0; i < n; i++) {
            semaphore2.acquire();
            printBar.run();
            semaphore.release();
        }
    }
}
