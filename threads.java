// Async = not occuring at the same time
// The Runnable interface should be implemented by any class whose instances are intended to be executed by a thread

// Static variables are like global variables, available to all instances
// Non static variables are like local variables, can be accessed only in instance of a class

// To use multiple threads in spring, use @Async
@Configuration
@EnableAsync
public class AsyncConfig {

    @Bean(name="taskExecutor")
    public Executor taskExecutor() {
        ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
         executor.setQueueCapacity(100); // when queue capacity full of tasks, cannot create more threads anymore
        executor.setMaxPoolSize(3); // max number of threads
         executor.setCorePoolSize(2); // standard number of threads
        executor.setThreadNamePrefix("poolThread-");
        executor.initialize();
        return executor;
    }
}
