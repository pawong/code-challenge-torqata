import platform
import psutil
import os

from typing import Any

from fastapi import Request


class SysInfoController:

    @staticmethod
    def get_platform_info():
        stats = [
            {'key': 'hostname', 'value': platform.node()},
            {'key': 'system os', 'value': platform.system()},
            {'key': 'os_version', 'value': platform.version()},
            {'key': 'py_version', 'value': platform.python_version()},
        ]
        return stats

    @staticmethod
    def get_memory_info():

        def to_megs(x):
            return round(float(x) / 1024**2, 2)

        virtual_memory = psutil.virtual_memory()
        swap_memory = psutil.swap_memory()
        stats = [
            {'key': 'virtual_total', 'value': to_megs(virtual_memory.total)},
            {'key': 'virtual_available', 'value': to_megs(virtual_memory.available)},
            {'key': 'swap_total', 'value': to_megs(swap_memory.total)},
            {'key': 'swap_used', 'value': to_megs(swap_memory.used)},
            {'key': 'swap_free', 'value': to_megs(swap_memory.free)},
        ]
        return stats

    @staticmethod
    def get_cpu_info():
        cpu_time = psutil.cpu_times()
        cpu_percent = psutil.cpu_times_percent(interval=1)
        stats = [
            {'key': 'num_cpus', 'value': psutil.cpu_count()},
            {'key': 'time_user', 'value': cpu_time.user},
            {'key': 'time_nice', 'value': cpu_time.nice},
            {'key': 'time_system', 'value': cpu_time.system},
            {'key': 'time_idle', 'value': cpu_time.idle},
            {'key': 'percent_user', 'value': cpu_percent.user},
            {'key': 'percent_nice', 'value': cpu_percent.nice},
            {'key': 'percent_system', 'value': cpu_percent.system},
            {'key': 'percent_idle', 'value': cpu_percent.idle},
        ]
        return stats

    @staticmethod
    def get_headers_info(request):
        retval = []
        for k, v in request.headers.items():
            retval.append({'key': k, 'value': v})
        return retval

    @staticmethod
    def get_release_info():
        deploy_directory = "NOT FOUND"
        git_revision = "NOT FOUND"
        try:
            deploy_directory = os.getcwd().split(os.path.sep)[-1]
            with open('REVISION', 'r') as f:
                git_revision = f.readline()
        except (OSError, IOError) as e:
            pass

        return [
            {'key': "deploy_directory", 'value': deploy_directory},
            {'key': "git_revision", 'value': git_revision},
        ]
