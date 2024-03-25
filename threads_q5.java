class H2O {

    private Semaphore hydrogenFlag = new Semaphore(2);
    private Semaphore oxygenFlag = new Semaphore(0);

    public H2O() {
        
    }

    public void hydrogen(Runnable releaseHydrogen) throws InterruptedException {
        hydrogenFlag.acquire();
        // releaseHydrogen.run() outputs "H". Do not change or remove this line.
        releaseHydrogen.run();
        oxygenFlag.release();
    }

    public void oxygen(Runnable releaseOxygen) throws InterruptedException {
        oxygenFlag.acquire(2);
        // releaseOxygen.run() outputs "O". Do not change or remove this line.
		releaseOxygen.run();
        hydrogenFlag.release(2);
    }
}
