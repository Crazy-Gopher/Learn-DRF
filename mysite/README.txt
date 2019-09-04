## https://realpython.com/asynchronous-tasks-with-django-and-celery/
## https://docs.celeryproject.org/en/latest/index.html

## Modify /etc/memcached.conf file to access memcache remotely:
1. find / -iname memcached.conf
/etc/memcached.conf
Then open the config file in your editor of choice:
2. vi /etc/memcached.conf
before update: -l 127.0.0.1
after update: -l 0.0.0.0


## Modify /etc/redis/redis.conf file to access Redis remotely:

1. cd /etc/redis
Then open the config file in your editor of choice:
2. vi redis.conf
before update: bind 127.0.0.1
after update: bind 0.0.0.0

## Modify /etc/postgresql/9.5/main/postgresql.conf file to access Postgresql remotely:
1. cd /etc/postgresql/9.5/main
Then open the config file in your editor of choice:
2. vi postgresql.conf
before update: listen_addresses = 'localhost'
after update: listen_addresses = '*'
3. vi pg_hba.conf
In order to fix it, open pg_hba.conf and add following entry at the very end.
host    all             all              0.0.0.0/0                       md5
host    all             all              ::/0                            md5(Optional)
The second entry is for IPv6 network.

# Configure supervisor https://www.digitalocean.com/community/tutorials/how-to-install-and-manage-supervisor-on-ubuntu-and-debian-vps

## Using Rabbitmq as a celery broker 

1. Command to start worker:
->celery -A mysite worker -l info

 -------------- celery@HJL010580 v4.3.0 (rhubarb)
---- **** -----
--- * ***  * -- Windows-10-10.0.17134-SP0 2019-07-19 19:54:10
-- * - **** ---
- ** ---------- [config]
- ** ---------- .> app:         mysite:0x49f85d0
- ** ---------- .> transport:   amqp://carousell:**@10.53.19.214:5672/carousell
- ** ---------- .> results:     disabled://
- *** --- * --- .> concurrency: 4 (prefork)
-- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
--- ***** -----
 -------------- [queues]
                .> celery           exchange=celery(direct) key=celery


[tasks]
  . mysite.celery.debug_task
  . polls.tasks.add
  . polls.tasks.create_random_user_accounts
  . polls.tasks.mul
  . polls.tasks.xsum

[2019-07-19 19:54:11,305: INFO/MainProcess] Connected to amqp://carousell:**@10.53.19.214:5672/carousell
[2019-07-19 19:54:11,383: INFO/MainProcess] mingle: searching for neighbors
[2019-07-19 19:54:12,492: INFO/MainProcess] mingle: all alone
[2019-07-19 19:54:12,570: WARNING/MainProcess] c:\users\kapil_jain\envs\djvenv\lib\site-packages\celery\fixups\django.py:202: UserWarning: Using settings.DEBUG leads to a memory leak, never use this setting in production environments!
  warnings.warn('Using settings.DEBUG leads to a memory leak, never '
[2019-07-19 19:54:12,570: INFO/MainProcess] celery@HJL010580 ready.
[2019-07-19 19:54:13,616: INFO/SpawnPoolWorker-1] child process 17064 calling self.run()
[2019-07-19 19:54:13,741: INFO/SpawnPoolWorker-4] child process 16492 calling self.run()
[2019-07-19 19:54:13,788: INFO/SpawnPoolWorker-3] child process 19248 calling self.run()
[2019-07-19 19:54:13,976: INFO/SpawnPoolWorker-2] child process 18980 calling self.run()

# Task Status
[2019-07-19 19:55:34,249: INFO/MainProcess] Received task: polls.tasks.create_random_user_accounts[f387af76-1adf-45ef-a89d-33061b615c59]
[2019-07-19 19:56:11,160: INFO/SpawnPoolWorker-3] Task polls.tasks.create_random_user_accounts[f387af76-1adf-45ef-a89d-33061b615c59] succeeded in 36.90699999999924s: '100 random users created with success!'


## Using Redis as a celery broker 

1. Command to start worker:
->celery -A mysite worker -l info

 -------------- celery@HJL010580 v4.3.0 (rhubarb)
---- **** -----
--- * ***  * -- Windows-10-10.0.17134-SP0 2019-07-19 22:23:46
-- * - **** ---
- ** ---------- [config]
- ** ---------- .> app:         mysite:0x4786a90
- ** ---------- .> transport:   redis://10.53.19.214:6379/0
- ** ---------- .> results:     disabled://
- *** --- * --- .> concurrency: 4 (prefork)
-- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
--- ***** -----
 -------------- [queues]
                .> celery           exchange=celery(direct) key=celery


[tasks]
  . mysite.celery.debug_task
  . polls.tasks.add
  . polls.tasks.create_random_user_accounts
  . polls.tasks.mul
  . polls.tasks.xsum

[2019-07-19 22:23:47,429: INFO/MainProcess] Connected to redis://10.53.19.214:6379/0
[2019-07-19 22:23:47,624: INFO/MainProcess] mingle: searching for neighbors
[2019-07-19 22:23:49,702: INFO/MainProcess] mingle: all alone
[2019-07-19 22:23:50,216: INFO/SpawnPoolWorker-4] child process 12716 calling self.run()
[2019-07-19 22:23:50,298: INFO/SpawnPoolWorker-3] child process 17924 calling self.run()
[2019-07-19 22:23:50,384: INFO/SpawnPoolWorker-1] child process 11376 calling self.run()
[2019-07-19 22:23:50,498: INFO/SpawnPoolWorker-2] child process 6640 calling self.run()
[2019-07-19 22:23:50,804: WARNING/MainProcess] c:\users\kapil_jain\envs\djvenv\lib\site-packages\celery\fixups\django.py:202: UserWarning: Using settings.DEBUG leads to a memory leak, never use this setting in production environments!
  warnings.warn('Using settings.DEBUG leads to a memory leak, never '
[2019-07-19 22:23:50,805: INFO/MainProcess] celery@HJL010580 ready.
[2019-07-19 22:25:02,048: INFO/MainProcess] Received task: polls.tasks.create_random_user_accounts[296d4e31-a93d-4c6e-8598-fc0eab38d3fc]
[2019-07-19 22:25:28,474: INFO/SpawnPoolWorker-4] Task polls.tasks.create_random_user_accounts[296d4e31-a93d-4c6e-8598-fc0eab38d3fc] succeeded in 26.42199999999866s: '51 random users created with success!'


## Execute a task from shell
(djvenv) C:\Users\kapil_jain\Psl-Django\mysite>python manage.py shell
Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from polls.tasks import add
>>> add.delay(10,20)
<AsyncResult: f47c0132-fd8b-4e92-b531-fafe9bf1cf47>
[2019-07-20 08:36:40,411: WARNING/MainProcess] Reset: Timezone changed from 'UTC' to None


# Celery beat
(djvenv) C:\Users\kapil_jain\Psl-Django\mysite>celery -A mysite beat -l info
celery beat v4.3.0 (rhubarb) is starting.
__    -    ... __   -        _
LocalTime -> 2019-07-20 09:57:33
Configuration ->
    . broker -> redis://10.53.19.214:6379/0
    . loader -> celery.loaders.app.AppLoader
    . scheduler -> celery.beat.PersistentScheduler
    . db -> celerybeat-schedule
    . logfile -> [stderr]@%INFO
    . maxinterval -> 5.00 minutes (300s)
[2019-07-20 09:57:33,093: INFO/MainProcess] beat: Starting...
[2019-07-20 09:57:33,268: INFO/MainProcess] Scheduler: Sending due task test_celery_beat (test_celery_beat)
[2019-07-20 09:58:00,001: INFO/MainProcess] Scheduler: Sending due task test_celery_beat (test_celery_beat)
[2019-07-20 09:59:00,000: INFO/MainProcess] Scheduler: Sending due task test_celery_beat (test_celery_beat)
[2019-07-20 10:00:00,000: INFO/MainProcess] Scheduler: Sending due task test_celery_beat (test_celery_beat)


# task send by celery beat and executed by celery worker

(djvenv) C:\Users\kapil_jain\Psl-Django\mysite>celery -A mysite worker -l info

 -------------- celery@HJL010580 v4.3.0 (rhubarb)
---- **** -----
--- * ***  * -- Windows-10-10.0.17134-SP0 2019-07-20 09:57:46
-- * - **** ---
- ** ---------- [config]
- ** ---------- .> app:         mysite:0x4da6b90
- ** ---------- .> transport:   redis://10.53.19.214:6379/0
- ** ---------- .> results:     disabled://
- *** --- * --- .> concurrency: 4 (prefork)
-- ******* ---- .> task events: OFF (enable -E to monitor tasks in this worker)
--- ***** -----
 -------------- [queues]
                .> celery           exchange=celery(direct) key=celery


[tasks]
  . mysite.celery.debug_task
  . polls.tasks.create_random_user_accounts
  . polls.tasks.mul
  . polls.tasks.xsum
  . send_feedback_email_task
  . sum_two_numbers
  . test_celery_beat

[2019-07-20 09:57:46,954: INFO/MainProcess] Connected to redis://10.53.19.214:6379/0
[2019-07-20 09:57:47,171: INFO/MainProcess] mingle: searching for neighbors
[2019-07-20 09:57:48,855: INFO/MainProcess] mingle: all alone
[2019-07-20 09:57:49,563: WARNING/MainProcess] c:\users\kapil_jain\envs\djvenv\lib\site-packages\celery\fixups\django.py:202: UserWarning: Using settings.DEBUG leads to a memory leak, never use this setting in production environments!
  warnings.warn('Using settings.DEBUG leads to a memory leak, never '
[2019-07-20 09:57:49,563: INFO/MainProcess] celery@HJL010580 ready.
[2019-07-20 09:57:49,629: INFO/SpawnPoolWorker-2] child process 24328 calling self.run()
[2019-07-20 09:57:49,663: INFO/MainProcess] Received task: test_celery_beat[f0fb167c-b043-41a6-8c74-2312f2e642e5]
[2019-07-20 09:57:49,781: INFO/SpawnPoolWorker-1] child process 22212 calling self.run()
[2019-07-20 09:57:49,784: INFO/SpawnPoolWorker-4] child process 16716 calling self.run()
[2019-07-20 09:57:49,812: INFO/SpawnPoolWorker-3] child process 20264 calling self.run()
[2019-07-20 09:57:52,544: INFO/SpawnPoolWorker-2] test_celery_beat[f0fb167c-b043-41a6-8c74-2312f2e642e5]: Current Time: 09:57AM on July 20, 2019
[2019-07-20 09:57:52,545: INFO/SpawnPoolWorker-2] Task test_celery_beat[f0fb167c-b043-41a6-8c74-2312f2e642e5] succeeded in 0.0s: None
[2019-07-20 09:58:00,078: INFO/MainProcess] Received task: test_celery_beat[256fa54f-dc2b-43db-9c25-170111b8be3a]
[2019-07-20 09:58:00,079: INFO/SpawnPoolWorker-2] test_celery_beat[256fa54f-dc2b-43db-9c25-170111b8be3a]: Current Time: 09:58AM on July 20, 2019
[2019-07-20 09:58:00,080: INFO/SpawnPoolWorker-2] Task test_celery_beat[256fa54f-dc2b-43db-9c25-170111b8be3a] succeeded in 0.0s: None
[2019-07-20 09:59:00,074: INFO/MainProcess] Received task: test_celery_beat[6784a920-33c4-4d1b-b26b-797750dc6fd3]
[2019-07-20 09:59:00,077: INFO/SpawnPoolWorker-4] test_celery_beat[6784a920-33c4-4d1b-b26b-797750dc6fd3]: Current Time: 09:59AM on July 20, 2019
[2019-07-20 09:59:00,081: INFO/SpawnPoolWorker-4] Task test_celery_beat[6784a920-33c4-4d1b-b26b-797750dc6fd3] succeeded in 0.0s: None
