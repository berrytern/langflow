from langflow.graph.schema import CHAT_COMPONENTS
from langflow.graph.vertex import types
from langflow.interface.agents.base import agent_creator
from langflow.interface.custom.base import custom_component_creator
from langflow.interface.document_loaders.base import documentloader_creator
from langflow.interface.embeddings.base import embedding_creator
from langflow.interface.llms.base import llm_creator
from langflow.interface.memories.base import memory_creator
from langflow.interface.prompts.base import prompt_creator
from langflow.interface.retrievers.base import retriever_creator
from langflow.interface.text_splitters.base import textsplitter_creator
from langflow.interface.toolkits.base import toolkits_creator
from langflow.interface.tools.base import tool_creator
from langflow.interface.wrappers.base import wrapper_creator
from langflow.utils.lazy_load import LazyLoadDictBase


class VertexTypesDict(LazyLoadDictBase):
    def __init__(self):
        self._all_types_dict = None

    @property
    def VERTEX_TYPE_MAP(self):
        return self.all_types_dict

    def _build_dict(self):
        langchain_types_dict = self.get_type_dict()
        return {
            **langchain_types_dict,
            "Custom": ["Custom Tool", "Python Function"],
        }

    def get_type_dict(self):
        return {
            **{t: types.PromptVertex for t in prompt_creator.to_list()},
            **{t: types.AgentVertex for t in agent_creator.to_list()},
            # **{t: types.ChainVertex for t in chain_creator.to_list()},
            **{t: types.ToolVertex for t in tool_creator.to_list()},
            **{t: types.ToolkitVertex for t in toolkits_creator.to_list()},
            **{t: types.WrapperVertex for t in wrapper_creator.to_list()},
            **{t: types.LLMVertex for t in llm_creator.to_list()},
            **{t: types.MemoryVertex for t in memory_creator.to_list()},
            **{t: types.EmbeddingVertex for t in embedding_creator.to_list()},
            # **{t: types.VectorStoreVertex for t in vectorstore_creator.to_list()},
            **{t: types.DocumentLoaderVertex for t in documentloader_creator.to_list()},
            **{t: types.TextSplitterVertex for t in textsplitter_creator.to_list()},
            **{t: types.CustomComponentVertex for t in custom_component_creator.to_list()},
            **{t: types.RetrieverVertex for t in retriever_creator.to_list()},
            **{t: types.InterfaceVertex for t in CHAT_COMPONENTS},
        }

    def get_custom_component_vertex_type(self):
        return types.CustomComponentVertex


lazy_load_vertex_dict = VertexTypesDict()
