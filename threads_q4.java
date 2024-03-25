class FizzBuzz {

    private int n;

    private int currentCount;

    private Semaphore fizzFlag = new Semaphore(0);
    private Semaphore buzzFlag = new Semaphore(0);
    private Semaphore fizzbuzzFlag = new Semaphore(0);
    private Semaphore numFlag = new Semaphore(1);

    public FizzBuzz(int n) {
        this.n = n;
        this.currentCount = 1;
    }

    private void lock() {
        currentCount++;
        if (currentCount <= n) {
            if (currentCount % 3 == 0 && currentCount % 5 != 0) {
                fizzFlag.release();
            } else if (currentCount % 3 != 0 && currentCount % 5 == 0) {
                buzzFlag.release();
            } else if (currentCount % 15 == 0) {
                fizzbuzzFlag.release();
            } else if (currentCount % 3 != 0 && currentCount % 5 != 0) {
                numFlag.release();
            }
        } else { // Must release Semaphore, which will cause all methods to run again, as while is constalty executing
            fizzFlag.release();
            buzzFlag.release();
            fizzbuzzFlag.release();
            numFlag.release();
        }
    }

    // printFizz.run() outputs "fizz".
    public void fizz(Runnable printFizz) throws InterruptedException {
        while (currentCount <= n) {
            fizzFlag.acquire();
            if (currentCount <= n) { // check for final release
                printFizz.run();
                lock();
            }
        }
    }

    // printBuzz.run() outputs "buzz".
    public void buzz(Runnable printBuzz) throws InterruptedException {
        while (currentCount <= n) {
            buzzFlag.acquire();
            if (currentCount <= n) {
                printBuzz.run();
                lock();
            }
        }
    }

    // printFizzBuzz.run() outputs "fizzbuzz".
    public void fizzbuzz(Runnable printFizzBuzz) throws InterruptedException {
        while (currentCount <= n) {
            fizzbuzzFlag.acquire();
            if (currentCount <= n) {
                printFizzBuzz.run();
                lock();
            }
        }
    }

    // printNumber.accept(x) outputs "x", where x is an integer.
    public void number(IntConsumer printNumber) throws InterruptedException {
        while (currentCount <= n) {
            numFlag.acquire();
            if (currentCount <= n) {
                printNumber.accept(currentCount);
                lock();
            }
        }
    }
}
