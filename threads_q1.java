// AtomicInteger as a counter (incrementAndGet) can be accessed concurrently by multiple threads
// Increases previous value by one, returns updated object

// Class Foo is passed to three different threads. How do we ensure first, second and third are called in correct order?
class Foo {

    public AtomicInteger threadCounter = new AtomicInteger();
    public AtomicInteger threadCounter2 = new AtomicInteger();

    public Foo() {

    }

    public void first(Runnable printFirst) throws InterruptedException {

        // printFirst.run() outputs "first". Do not change or remove this line.
        printFirst.run();
        threadCounter.incrementAndGet();
    }

    public void second(Runnable printSecond) throws InterruptedException {
        while (threadCounter.get() != 1) {

        }
        // printSecond.run() outputs "second". Do not change or remove this line.
        printSecond.run();
        threadCounter2.incrementAndGet();
    }

    public void third(Runnable printThird) throws InterruptedException {
        while (threadCounter2.get() != 1) {

        }
        // printThird.run() outputs "third". Do not change or remove this line.
        printThird.run();
    }
}



