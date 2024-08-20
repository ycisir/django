# =============================== custom signal ============================================

# from django.dispatch import Signal, receiver

# # creating signal
# notification = Signal(providing_args=["request", "user"])


# # receiver function
# @receiver(notification)
# def show_notification(sender, **kwargs):
#     print(sender)
#     print(f'{kwargs}')
#     print('Notification')



# ==========================================================================================

# from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
# from django.contrib.auth.models import User
# from django.dispatch import receiver
# from django.db.models.signals import pre_init, pre_save, pre_delete, post_init, post_save, post_delete, pre_migrate, post_migrate
# from django.core.signals import request_started, request_finished, got_request_exception
# from django.db.backends.signals import connection_created



# # ======================== login / logout ====================================
# @receiver(user_logged_in, sender=User)
# def login_success(sender, request, user, **kwargs):
#     print('=='*30)
#     print('Logged in signal running...')
#     print(f'Sender : {sender}')
#     print(f'Request : {request}')
#     print(f'User : {user}')
#     print(f'User password : {user.password}')
#     print(f'Kwargs : {kwargs}')
#     print('=='*30)

# @receiver(user_logged_out, sender=User)
# def log_out(sender, request, user, **kwargs):
#     print('=='*30)
#     print('Logged out signal running...')
#     print(f'Sender : {sender}')
#     print(f'Request : {request}')
#     print(f'User : {user}')
#     print(f'User password : {user.password}')
#     print(f'Kwargs : {kwargs}')
#     print('=='*30)

# @receiver(user_login_failed)
# def login_failed(sender, credentials, request, **kwargs):
#     print('=='*30)
#     print('Log in failed signal running...')
#     print(f'Sender : {sender}')
#     print(f'Credentials : {credentials}')
#     print(f'Request : {request}')
#     print(f'Kwargs : {kwargs}')
#     print('=='*30)

# # user_logged_in.connect(login_success, sender=User)

# # ===========================================================================


# # ======================== pre save / post save ====================================

# @receiver(pre_save, sender=User)
# def at_begining_save(sender, instance, **kwargs):
#     print('=='*30)
#     print('Pre save signal running...')
#     print(f'Sender : {sender}')
#     print(f'Instance : {instance}')
#     print(f'Kwargs : {kwargs}')
#     print('=='*30)
#     # pre_save.connect(at_begining_save, sender=User)


# @receiver(post_save, sender=User)
# def at_ending_save(sender, instance, created, **kwargs):
#     if created:
#         print('=='*30)
#         print('Post save signal running...')
#         print('New record')
#         print(f'Sender : {sender}')
#         print(f'Instance : {instance}')
#         print(f'Created : {created}')
#         print(f'Kwargs : {kwargs}')
#         print('=='*30)
#     else:
#         print('=='*30)
#         print('Post save signal running...')
#         print('Update')
#         print(f'Sender : {sender}')
#         print(f'Instance : {instance}')
#         print(f'Created : {created}')
#         print(f'Kwargs : {kwargs}')
#         print('=='*30)

#     # pre_save.connect(at_begining_save, sender=User)

# # ===========================================================================

# # ======================== pre delete / post delete ====================================

# @receiver(pre_delete, sender=User)
# def at_begining_delete(sender, instance, **kwargs):
#     print('=='*30)
#     print('Pre delete signal running...')
#     print(f'Sender : {sender}')
#     print(f'Instance : {instance}')
#     print(f'Kwargs : {kwargs}')
#     print('=='*30)
#     # pre_delete.connect(at_begining_delete, sender=User)


# @receiver(post_delete, sender=User)
# def at_ending_delete(sender, instance, **kwargs):
#     print('=='*30)
#     print('Post delete signal running...')
#     print(f'Sender : {sender}')
#     print(f'Instance : {instance}')
#     print(f'Kwargs : {kwargs}')
#     print('=='*30)

#     # post_delete.connect(at_begining_delete, sender=User)
    
# # ===========================================================================

# # ======================== pre init / post init ====================================

# # @receiver(pre_init, sender=User)
# # def at_begining_init(sender, *args, **kwargs):
# #     print('=='*30)
# #     print('Pre init signal running...')
# #     print(f'Sender : {sender}')
# #     print(f'Args : {args}')
# #     print(f'Kwargs : {kwargs}')
# #     print('=='*30)
# #     # pre_init.connect(at_begining_init, sender=User)


# # @receiver(post_init, sender=User)
# # def at_ending_init(sender, *args, **kwargs):
# #     print('=='*30)
# #     print('Post init signal running...')
# #     print(f'Sender : {sender}')
# #     print(f'Args : {args}')
# #     print(f'Kwargs : {kwargs}')
# #     print('=='*30)

#     # post_init.connect(at_begining_init, sender=User)


# # ===========================================================================

# # ======================== pre request / post request ====================================

# # @receiver(request_started)
# # def at_begining_request(sender, environ, **kwargs):
# #     print('=='*30)
# #     print('At begining request...')
# #     print(f'Sender : {sender}')
# #     print(f'Environ : {environ}')
# #     print(f'Kwargs : {kwargs}')
# #     print('=='*30)
#     # request_started.connect(at_begining_request, sender=User)


# # @receiver(request_finished)
# # def at_ending_request(sender, **kwargs):
# #     print('=='*30)
# #     print('At ending request...')
# #     print(f'Sender : {sender}')
# #     print(f'Kwargs : {kwargs}')
# #     print('=='*30)

#     # request_finished.connect(at_ending_request, sender=User)


# # @receiver(got_request_exception)
# # def at_req_exception(sender, request, **kwargs):
# #     print('=='*30)
# #     print('At request exception...')
# #     print(f'Sender : {sender}')
# #     print(f'Request : {request}')
# #     print(f'Kwargs : {kwargs}')
# #     print('=='*30)

#     # got_request_exception.connect(at_req_exception, sender=User)

# # ===========================================================================

# # ======================== pre migrate / post migrate ====================================

# # @receiver(pre_migrate)
# # def before_install_app(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
# #     print('=='*30)
# #     print('before_install_app')
# #     print(f'Sender : {sender}')
# #     print(f'app_config : {app_config}')
# #     print(f'verbosity : {verbosity}')
# #     print(f'interactive : {interactive}')
# #     print(f'using : {using}')
# #     print(f'plan : {plan}')
# #     print(f'apps : {apps}')
# #     print(f'Kwargs : {kwargs}')
# #     print('=='*30)

#     # pre_migrate.connect(before_install_app, sender=User)


# # @receiver(post_migrate)
# # def at_end_migrate_flush(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
# #     print('=='*30)
# #     print('at_end_migrate_flush')
# #     print(f'Sender : {sender}')
# #     print(f'app_config : {app_config}')
# #     print(f'verbosity : {verbosity}')
# #     print(f'interactive : {interactive}')
# #     print(f'using : {using}')
# #     print(f'plan : {plan}')
# #     print(f'apps : {apps}')
# #     print(f'Kwargs : {kwargs}')
# #     print('=='*30)

#     # post_migrate.connect(before_install_app, sender=User)


# # ===========================================================================

# # ======================== connection created ====================================

# @receiver(connection_created)
# def conn_db(sender, connection, **kwargs):
#     print('=='*30)
#     print('Initial connection to database...')
#     print(f'Sender : {sender}')
#     print(f'connection : {connection}')
#     print(f'Kwargs : {kwargs}')
#     print('=='*30)

#     # connection_created.connect(conn_db)