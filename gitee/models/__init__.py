# coding: utf-8

# flake8: noqa
"""
    码云 Open API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 5.3.2

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from gitee.models.basic_info import BasicInfo
from gitee.models.blob import Blob
from gitee.models.branch import Branch
from gitee.models.branch_commit import BranchCommit
from gitee.models.branch_protection_put_param import BranchProtectionPutParam
from gitee.models.code import Code
from gitee.models.code_comment import CodeComment
from gitee.models.code_forks import CodeForks
from gitee.models.code_forks_history import CodeForksHistory
from gitee.models.commit import Commit
from gitee.models.commit_content import CommitContent
from gitee.models.commit_tree import CommitTree
from gitee.models.compare import Compare
from gitee.models.complete_branch import CompleteBranch
from gitee.models.content import Content
from gitee.models.content_basic import ContentBasic
from gitee.models.contributor import Contributor
from gitee.models.create_branch_param import CreateBranchParam
from gitee.models.create_pull_request_param import CreatePullRequestParam
from gitee.models.email import Email
from gitee.models.enterprise_basic import EnterpriseBasic
from gitee.models.enterprise_member import EnterpriseMember
from gitee.models.event import Event
from gitee.models.git_commit import GitCommit
from gitee.models.git_user import GitUser
from gitee.models.group import Group
from gitee.models.group_detail import GroupDetail
from gitee.models.group_member import GroupMember
from gitee.models.hook import Hook
from gitee.models.issue import Issue
from gitee.models.issue_comment_patch_param import IssueCommentPatchParam
from gitee.models.issue_comment_post_param import IssueCommentPostParam
from gitee.models.issue_create_param import IssueCreateParam
from gitee.models.issue_update_param import IssueUpdateParam
from gitee.models.label import Label
from gitee.models.label_post_param import LabelPostParam
from gitee.models.milestone import Milestone
from gitee.models.namespace import Namespace
from gitee.models.namespace_mini import NamespaceMini
from gitee.models.new_file_param import NewFileParam
from gitee.models.note import Note
from gitee.models.operate_log import OperateLog
from gitee.models.program_basic import ProgramBasic
from gitee.models.project import Project
from gitee.models.project_basic import ProjectBasic
from gitee.models.project_label import ProjectLabel
from gitee.models.project_member import ProjectMember
from gitee.models.project_member_permission import ProjectMemberPermission
from gitee.models.project_member_permission_detail import ProjectMemberPermissionDetail
from gitee.models.project_member_put_param import ProjectMemberPutParam
from gitee.models.pull_request import PullRequest
from gitee.models.pull_request_assignee_post_param import PullRequestAssigneePostParam
from gitee.models.pull_request_comment_patch_param import PullRequestCommentPatchParam
from gitee.models.pull_request_comment_post_param import PullRequestCommentPostParam
from gitee.models.pull_request_comments import PullRequestComments
from gitee.models.pull_request_commits import PullRequestCommits
from gitee.models.pull_request_file_path import PullRequestFilePath
from gitee.models.pull_request_files import PullRequestFiles
from gitee.models.pull_request_label_post_param import PullRequestLabelPostParam
from gitee.models.pull_request_merge_put_param import PullRequestMergePutParam
from gitee.models.pull_request_update_param import PullRequestUpdateParam
from gitee.models.release import Release
from gitee.models.repo_commit import RepoCommit
from gitee.models.repo_patch_param import RepoPatchParam
from gitee.models.repository_post_param import RepositoryPostParam
from gitee.models.ssh_key import SSHKey
from gitee.models.ssh_key_basic import SSHKeyBasic
from gitee.models.set_repo_reviewer import SetRepoReviewer
from gitee.models.single_commit import SingleCommit
from gitee.models.tag import Tag
from gitee.models.tree import Tree
from gitee.models.tree_basic import TreeBasic
from gitee.models.user import User
from gitee.models.user_basic import UserBasic
from gitee.models.user_message import UserMessage
from gitee.models.user_message_list import UserMessageList
from gitee.models.user_mini import UserMini
from gitee.models.user_notification import UserNotification
from gitee.models.user_notification_count import UserNotificationCount
from gitee.models.user_notification_list import UserNotificationList
from gitee.models.user_notification_namespace import UserNotificationNamespace
from gitee.models.user_notification_subject import UserNotificationSubject
from gitee.models.week_report import WeekReport
from gitee.models.week_report_id_body import WeekReportIdBody
from gitee.models.week_report_id_body1 import WeekReportIdBody1
from gitee.models.model_issue import Issue
from gitee.models.model_milestone import Milestone
from gitee.models.model_program_basic import ProgramBasic
from gitee.models.model_user_basic import UserBasic
from gitee.models.model_label import Label
from gitee.models.hook_event_models import IssueHook
from gitee.models.hook_event_models import ProjectHook
from gitee.models.hook_event_models import CommitHook
from gitee.models.hook_event_models import LabelHook
from gitee.models.hook_event_models import UserHook
from gitee.models.hook_event_models import EnterpriseHook
from gitee.models.hook_event_models import NoteHook
from gitee.models.hook_event_models import MilestoneHook
from gitee.models.hook_event_models import BranchHook
from gitee.models.hook_event_models import PullRequestHook
from gitee.models.hook_event_types import NoteEvent
from gitee.models.hook_event_types import NoteEvent
from gitee.models.hook_event_types import IssueEvent
from gitee.models.hook_event_types import RepoInfo
from gitee.models.hook_event_types import PullRequestEvent
from gitee.models.hook_event_types import PushEvent
from gitee.models.hook_event_types import TagPushEvent
from gitee.models.hook_event_helper import EVENT_TYPE_NOTE
from gitee.models.hook_event_helper import EVENT_TYPE_PUSH
from gitee.models.hook_event_helper import EVENT_TYPE_ISSUE
from gitee.models.hook_event_helper import EVENT_TYPE_PR
from gitee.models.hook_event_helper import STATUS_OPEN
from gitee.models.hook_event_helper import STATUS_CLOSED
from gitee.models.hook_event_helper import STATUS_MERGED
from gitee.models.hook_event_helper import ACTION_OPEN
from gitee.models.hook_event_helper import ACTION_CLOSE
from gitee.models.hook_event_helper import PR_ACTION_MERGE
from gitee.models.hook_event_helper import PR_ACTION_UPDATED_LABEL
from gitee.models.hook_event_helper import PR_ACTION_CHANGED_TARGET_BRANCH
from gitee.models.hook_event_helper import PR_ACTION_CHANGED_SOURCE_BRANCH
from gitee.models.hook_event_helper import ACTION_ADD_LABEL
from gitee.models import converter
