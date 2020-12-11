// This is a multithreading model implemented via POSIX standard semaphores.
// It creates 2 * (CPU cores) worker threads.
// Once a thread has ended, it creates another, as long as the number of 
// worker threads is no more than the max number of allowed threads.


#include <pthread.h>
#include <stdio.h>

int get_cpu_count();

int main(int argc, char *argv[])
{
    int max_threads_count = get_cpu_count();
    pthread_t worker_threads[max_threads_count];
    int thread_slot = max_threads_count - 1; // thread slot is zero-based
    
    // init conditions
    sem_t idle_threads;
    sem_init(&idle_threads, 0, max_threads_count);
    
    for (; ;) {
        // greedy thread creation
        for (; ;) {
            if (0 == sem_trywait(idle_threads)) {
                pthread_create(&worker_threads[thread_slot], NULL, worker_thread_main, &thread_slot);
                --thread_slot;
            }
            else
                break;  // no idle threads
        }
        
        if (0 == pthread_join())
    }
}


// to be implemented
int get_cpu_count()
{
    return 4;
}

void * worker_thread_main(void *arg)
{

}