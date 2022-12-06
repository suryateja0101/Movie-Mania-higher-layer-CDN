import random


class AuthRouter:

    route_app_labels = {'auth', 'contenttypes',
                        'sessions', 'admin', 'baseapp'}  # 'baseapp'

    def db_for_read(self, model, **hints):
        # """
        # Attempts to read auth and contenttypes models go to auth_db.
        # """
        if model._meta.app_label in self.route_app_labels:
            return 'primary'  # random.choice(['replica1', 'primary'])
        return None

    def db_for_write(self, model, **hints):
        # """
        # Attempts to write auth and contenttypes models go to auth_db.
        # """
        if model._meta.app_label in self.route_app_labels:
            return 'primary'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        # """
        # Allow relations if a model in the auth or contenttypes apps is
        # involved.
        # """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # """
        # Make sure the auth and contenttypes apps only appear in the
        # 'auth_db' database.
        # """
        if app_label in self.route_app_labels:
            return True  # db == 'primary'
        return None


# class PrimaryReplicaRouter:
#     route_app_labels = {'auth', 'contenttypes', 'sessions', 'baseapp', 'auth'}

#     def db_for_read(self, model, **hints):
#         # """
#         # Attempts to read auth and contenttypes models go to auth_db.
#         # """
#         # if model._meta.app_label in self.route_app_labels:
#         return 'replica1'
#         #random.choice(['replica1', 'primary'])

#     def db_for_write(self, model, **hints):
#         # """
#         # Attempts to write auth and contenttypes models go to auth_db.
#         # """
#         if model._meta.app_label in self.route_app_labels:
#             return 'replica1'
#         return False

#     def allow_relation(self, obj1, obj2, **hints):
#         # """
#         # Allow relations if a model in the auth or contenttypes apps is
#         # involved.
#         # """
#         if (
#             obj1._meta.app_label in self.route_app_labels or
#             obj2._meta.app_label in self.route_app_labels
#         ):
#             return True
#         return None

#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         # """
#         # Make sure the auth and contenttypes apps only appear in the
#         # 'auth_db' database.
#         # """
#         if app_label in self.route_app_labels:
#             return True  # db == 'primary'
#         return None
